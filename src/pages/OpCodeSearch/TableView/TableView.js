import React from 'react'
import './TableView.css';

const Table = ({template, tableData}) => {

  return (
    <div>
        <div>
        { template &&
          template.tableComponent && template.tableComponent.tableCol &&
            <>
              <table className='table-style'>
                <thead>
                  <tr>
                    {
                      template &&
                      template.tableComponent.tableCol.map((item, index) =>
                        <th key={index} style={{width: item.size, maxWidth: item.size}}>{
                          item.title
                        }</th>
                      )
                    }
                  </tr>
                </thead>
                <tbody>
                  { tableData &&
                    tableData.map((user, userIndex) =>
                      <tr key={userIndex}>
                        {
                          template.tableComponent.tableCol.map((item, index) =>
                            <td key={index} style={{width: item.size, maxWidth: item.size}}>{user[item.key]}</td>
                          )
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
            </>
        }
      </div>
    </div>
  )
}

export default Table