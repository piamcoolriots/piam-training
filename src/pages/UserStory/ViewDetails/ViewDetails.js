import React, { useEffect, useState } from 'react'
import { SERVER } from '../../../utils/server';
import './ViewDetails.css';

const ViewDetails = ({data, setStoryDataFunc, changeFrame, changeUrlParameter}) => {
  const [viewDetails, setViewDetails] = useState({});

  // const [searchParams, setSearchParams] = useSearchParams();
  // console.log(searchParams);
  // console.log(previousFrameContext);

	useEffect(() => {
			if(data.user_id !== "" && data.fields.length !== 0) {
        fetch(`${SERVER}/api/viewDetails`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        })
        .then(res => res.json())
        .then(result => {
          setViewDetails(result);
          if(result !== undefined && data.target !== undefined) {
            setStoryDataFunc({target: data.target, result: result});
          }
        });
      } else {
        setViewDetails({});
      }
		console.log(viewDetails);
	}, [data.user_id]);

  const parameterValue = (contextField, data) => {
    let paramValue = "";
    contextField.forEach((value) => {
        if(data[value] !== undefined) {
            if(paramValue === "") {
              paramValue = data[value];
            } else {
              paramValue = paramValue + "," + data[value];
            }
        }
    })
    return paramValue;
}


  return (
    <div>
      {
        Object.keys(viewDetails).length !== 0 &&
        <>
          {
            data.fields.map((item, index) =>
              <div key={index}>
                <h3>{item?.title}</h3>
                <p style={{whiteSpace: 'wrap' }}>{viewDetails[item?.key]}</p>
              </div>
            )
          }
          {/* <div>
            <br />
            <p>{data?.target}</p>
            <p >{viewDetails[data?.contextField[0]]}</p>
          </div> */}
          <div className='button-container'>
            <button onClick={() => {changeFrame(); changeUrlParameter(data?.target, parameterValue(data?.contextField, viewDetails))}} className='next-button'>Next</button>
          </div>
        </>
      }
    </div>
  )
}

export default ViewDetails