/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect, useState } from 'react';
import axios from 'axios';
import Table from '../TableView/TableView';
import './OpCodeSearch.css';
import Pagination from '../../../components/Pagination/Pagination';
import DropDown from '../../../components/DropDown/DropDown';
import { SERVER } from '../../../utils/server';
import { useQuery } from '@tanstack/react-query';
import Skeleton from '../../../components/Loading/Skeleton';

const OpCodeSearch = ({templateName, setFields, setUserId, previousFrameContext}) => {
  const urlParams = new URLSearchParams(window.location.search);
  const [windowWidth, setWindowWidth] = useState(window.innerWidth);

  const [page, setPage] = useState(1); // State to hold current page number

  const [template, setTemplate] = useState({
      "templateName": "",
      "tableName": "",
      "searchComponent": {},
      "tableComponent": {},
  });
  
  const [formData, setFormData] = useState({}); // State to hold search input values

  const [tableData, setTableData] = useState([]); // State to store table data
  const [totalPage, setTotalPage] = useState(0); // State to store total page number

  const [showTable, setShowTable] = useState(false);

  const filterDataFunc = (searchComponent, formData) => {
    const { condition, fields } = searchComponent;

    const filterData = {
      logicalOperator: condition,
      rules: formData && Object.keys(formData).map((key) => {
        const field = fields.find((field) => field.key === key);
        const rule = {
          field: field.key,
          dataType: field.dataType,
          comparisonOperator: field.operator,
          value: formData[key],
        };
        if(field.connection) {
          rule.connection = field.connection;
        }
        return rule;
      }, {}),
    };
    // console.log(filterData);

    return filterData;
  }

  
  useEffect(() => {
    handleClear();
  }, [templateName]);
  

  const {} = useQuery({
    queryKey: ['template', templateName],
    queryFn: () => axios.get(`${SERVER}/api/template?templateName=${templateName}`).then((res) => {
      if(Object.keys(previousFrameContext).length !== 0) {
        const previousFrameName = previousFrameContext.frameTemplateName;
        const previousFrameContextField = previousFrameContext.contextField;
        const paramValue = urlParams.get(previousFrameName);
        const previousFrameContextValue = paramValue.split(',');
        let data = {};
        previousFrameContextValue.forEach((value, index) => {
          data[previousFrameContextField[index]] = value;
        });
        setFormData(data);
      }
      setTemplate(res.data);
      setFields(res.data.viewDetailComponent.fields);
    }),
  });

  // useEffect(() => {
  //   if(Object.keys(previousFrameContext).length !== 0) {
  //     const previousFrameName = previousFrameContext.frameTemplateName;
  //     const previousFrameContextField = previousFrameContext.contextField;
  //     const paramValue = urlParams.get(previousFrameName);
  //     const previousFrameContextValue = paramValue.split(',');
  //     const data = {};
  //     previousFrameContextValue.forEach((value, index) => {
  //       data[previousFrameContextField[index]] = value;
  //     });
  //     setFormData(data);
  //   }
  // }, [template]);

  const changePage = (page) => {
    setPage(page);
    axios.post(`${SERVER}/api/tableData`, 
        {
          target: template.tableName,
          action: 'search',
          filter: filterDataFunc(template.searchComponent, formData),
          columnsToRetrieve: template.tableComponent.tableCol,
          resultDisplayOrder: template.tableComponent.displayOrder,
          maxRowsPerPage: template.tableComponent.maxRow,
          pageToRetrieve: page - 1,
        }
      ).then((res) => {
        setTableData(res.data.tableRow);
        setTotalPage(res.data.totalPage);
      })
    
  };
  
  
  // Function to handle search input values
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };
  
  // Function to fetch data based on search input values
  const handleSubmit = () => {
    setPage(1);
    const payLoad = {
      target: template.tableName,
      action: 'search',
      filter: filterDataFunc(template.searchComponent, formData),
      columnsToRetrieve: template.tableComponent.tableCol,
      resultDisplayOrder: template.tableComponent.displayOrder,
      maxRowsPerPage: template.tableComponent.maxRow,
      pageToRetrieve: page - 1,
    };
    axios.post(`${SERVER}/api/tableData`,
      payLoad
    ) 
      .then(
        (response) => {
          setTableData(response.data.tableRow);
          setTotalPage(response.data.totalPage);
          setShowTable(true);
        },
        (error) => {
          console.log(error);
        }
      )
  };

  // Function to clear search input values and fetch all data
  const handleClear = () => {
    setFormData({});
    setPage(1);
    setShowTable(false);
    setUserId('');
    if(Object.keys(previousFrameContext).length !== 0) {
      const previousFrameName = previousFrameContext.frameTemplateName;
      const previousFrameContextField = previousFrameContext.contextField;
      const previousFrameContextValue = urlParams.get(previousFrameName).split(',');
      let data = {};
      previousFrameContextValue.forEach((value, index) => {
        data[previousFrameContextField[index]] = value;
      });
      setFormData(data);
      // console.log(previousFrameContextValue);
    }
  };
    
  return (
    template.tableName !== ""?
    <div>
      <div>
        {
          template && template.searchComponent && template.searchComponent.fields && template.searchComponent.fields.length > 0 &&
          <div className='search-container'>
            <div className='fields-container'>
              {
                template.searchComponent && template.searchComponent.fields &&
                template.searchComponent.fields.map((item, index) =>
                  <div key={index} className='field-container' style={{gridColumn: `${windowWidth > 700 ? `span ${item?.size}`: 'span 1'}`}}>
                    {
                      ['text', 'number', 'date', 'email'].includes(item.type) &&
                      <div className='container-item'>
                        <label for={item.key} className='field-title'>{item.label}</label>
                        <input
                          type={item.type}
                          name={item.key}
                          id={item.key}
                          placeholder={item.placeholder}
                          value={formData[item.key] || ''}
                          onChange={handleInputChange}  
                          style={{width: `${item?.width ? item?.width : '100%'}`}}
                          className='input-box'
                        />
                      </div>
                    }
                    {
                      item.type === 'dropdown' &&
                      <div className='container-item'>
                        <label for={item.key} className='field-title'>{item.label}</label>
                        <DropDown id={item.key} item={item} formData={formData} handleInputChange={handleInputChange} />
                      </div>
                    }
                    {
                      item.type === 'radio' &&
                      <div className='container-item'>
                        <label className='field-title'>{item.label}</label>
                        <div id={item.key} className='radio-container'>
                          {
                            item.values.map((value, index) =>
                              <div key={index}>
                                <input
                                  type="radio"
                                  id={value}
                                  name={item.key}
                                  value={value}
                                  checked={formData[item.key] === value}
                                  onChange={handleInputChange}
                                />
                                <label htmlFor={value}>{value}</label>
                              </div>
                            )
                          }
                        </div>
                      </div>
                    }
                  </div>
                )
              }
            </div>
            <div>
              {
                template.searchComponent && template.searchComponent.fields &&
                <div className='button-container'>
                  <div>
                    <button onClick={handleSubmit} className='submit-button'>Search</button>
                    <button onClick={handleClear} className='clear-button'>Clear</button>
                  </div>
                </div>
              }
            </div>
          </div>
        }
      </div>
      <div>
        {
          tableData && showTable  &&
          <div >
            <div>
              <div>
                <div className='table-container'>
                  <Table template={template} tableData={tableData} setUserId={setUserId} />
                </div>
              </div>
            </div>
            {
              tableData && tableData.length > 0 && totalPage > 0 &&
              <div className='pagination-style' >
                <Pagination 
                  currentPage={page}
                  totalPages={totalPage}
                  onPageChange={page => changePage(page)}
                  className='pagination-style'
                />
              </div>
            }
            
          </div>
        }
      </div>
    </div>
    :
    <div>
      <Skeleton></Skeleton>
    </div>
  );
}

export default OpCodeSearch