import React from 'react'
import './TableView.css';
import { AiFillCheckCircle } from 'react-icons/ai';
import { CgRadioCheck } from 'react-icons/cg';
import { Modal } from '../../../components/Modal/Modal';
import OpCodeEdit from '../../OpCodeEdit/OpCodeEdit';

const Table = ({template, tableData, setUserId}) => {
  const [toggleButtonId, setToggleButtonId] = React.useState(null);
  const [showModal, setShowModal] = React.useState(false);
  const [editRecordId, setEditRecordId] = React.useState(null);


  const handleRowClick = (userId) => { 
    setToggleButtonId(userId);
    setUserId(userId);
  }
  
  return (
    <div className="table-container">
      { template &&
        template.tableComponent && template.tableComponent.tableCol &&
          <>
            <div className="table-scroll">
              <table className='table-style'>
                <thead>
                  <tr>
                    {
                      template &&
                      <>
                        {
                          <th></th>
                        }
                        {
                          template.tableComponent.tableCol.map((item, index) =>
                            <th key={index} style={{width: item.size, maxWidth: item.size}}>{
                              item.title
                            }</th>
                          )
                        }
                        {
                          <th></th>
                        }
                      </>
                    }
                  </tr>
                </thead>
                <tbody>
                  { tableData &&
                    tableData.map((user, userIndex) =>
                      <tr key={userIndex}>
                        {
                          <td  style={{width: '30px', textAlign: 'center'}}>
                            <div onClick={() => handleRowClick(user._id)} className='toggle-button'>
                              {
                                toggleButtonId === user._id ? 
                                  <AiFillCheckCircle className='toggle-active' /> 
                                    : 
                                  <CgRadioCheck className='toggle-inactive' />
                              }
                            </div>
                          </td>
                        }
                        {
                          template.tableComponent.tableCol.map((item, index) =>
                            <td key={index} style={{width: item.size, maxWidth: item.size}}>{user[item.key]}</td>
                          )
                        }
                        {
                          <th style={{width: '50px', textAlign: 'center'}}>
                            <button onClick={() => {setShowModal((prev) => !prev); setEditRecordId(user._id)}}>Edit</button>
                          </th>
                        }
                      </tr>
                    )
                  }
                </tbody>
              </table>
              <>
                {
                  tableData && tableData.length === 0 &&
                  <div className='no-data'>No data found!</div>
                }
              </>
            </div>
            {
              tableData && tableData.length > 0 && 
              <Modal open={showModal} onClose={() => setShowModal((prev) => !prev)}>
                <OpCodeEdit template={template} recordId={editRecordId} />
              </Modal>
            }
          </>
      }
    </div>
  )
}

export default Table