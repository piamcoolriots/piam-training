import React, { useState, useEffect } from 'react';
import DropDown from '../../components/DropDown/DropDown';
import {SERVER} from '../../utils/server';
import axios from 'axios';
import Validate from '../../Validation/validate';

const OpCodeEdit = ({template, recordId}) => {
    const [reload, setReload] = useState(true);
    const [data, setData] = useState({});
    
    const [windowWidth, setWindowWidth] = useState(window.innerWidth);
    useEffect(() => { 
      const handleResize = () => setWindowWidth(window.innerWidth);
      window.addEventListener("resize", handleResize);
      return () => window.removeEventListener("resize", handleResize);
    }, []);
    
  
    // Fetch template data from the server
    useEffect(() => {
      axios.post(`${SERVER}/api/getRecord`, {
        tableName: template.tableName,
        ID: recordId
      })
        .then(
          (response) => {
            console.log(response.data)
            setReload(false);
            setData(response.data);
          },
          (error) => {
            console.log(error);
          }
        )
    }, [reload]);
  
    // Function to handle search input values
    const handleInputChange = (e) => {
      const { name, value } = e.target;
      setData({ ...data, [name]: value });
    };

    console.log(data['traineeId']);
      
    return (
      <div>
        <div>
          {
            template && template.formComponent && template.formComponent.fields && template.formComponent.fields.length > 0 &&
            <div className='search-container'>
              <div className='fields-container'>
                {
                  template.formComponent && template.formComponent.fields &&
                  template.formComponent.fields.map((item, index) =>
                    <div key={index} className='field-container' style={{gridColumn: `${windowWidth > 700 ? `span ${item?.size}`: 'span 1'}`}}>
                      {
                        ['text', 'number', 'date', 'email'].includes(item.type) &&
                        <div className='container-item'>
                          <label htmlFor={item.key} className='field-title'>{item.label}</label>
                          <input
                            type={item.type}
                            name={item.key}
                            placeholder={item.placeholder}
                            value={( data[item.key] ) || ""}
                            onChange={handleInputChange}  
                            style={{width: `${item?.width ? item?.width : '100%'}`}}
                            className='input-box'
                          />
                          <p>{Validate(item.type, data[item.key])}</p>
                        </div>
                      }
                      {
                        item.type === 'dropdown' &&
                        <div className='container-item'>
                          <label htmlFor={item.key} className='field-title'>{item.label}</label>
                          <DropDown item={item}  data={data}  handleInputChange={handleInputChange} />
                        </div>
                      }
                      {
                        item.type === 'radio' &&
                        <div className='container-item'>
                          <label className='field-title'>{item.label}</label>
                          <div className='radio-container'>
                            {
                              item.values.map((value, index) =>
                                <div key={index}>
                                  <input
                                    type="radio"
                                    id={value}
                                    name={item.key}
                                    value={value}
                                    checked={data[item.key] === value}
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
              {/* <div>
                {
                  template.formComponent && template.formComponent.fields &&
                  <div className='button-container'>
                    <div>
                      <button onClick={handleSubmit} className='submit-button'>Submit</button>
                      <button onClick={handleClear} className='clear-button'>Clear</button>
                    </div>
                  </div>
                }
              </div> */}
            </div>
          }
        </div>
      </div>
    );
}

export default OpCodeEdit