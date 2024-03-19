import React, { useEffect, useState } from 'react';
import OpCodeSearch from './OpCodeSearch/OpCodeSearch';
import ViewDetails from './ViewDetails/ViewDetails';
import { useNavigate, useSearchParams } from 'react-router-dom';
import './UserStory.css';

const UserStory = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const navigate = useNavigate();

  const changeUrlParameter = (parameter, value) => {
    const currentParams = new URLSearchParams(searchParams);
    currentParams.set(parameter, value);
    navigate(`?${currentParams.toString()}`);
  };

  const [previousFrameContext, setPreviousFrameContext] = useState({});

  const [storyTemplate, setStoryTemplate] = useState({
    storyTemplateNumber: '',
    title: '',
    frames: [],
  });
  const [frameData, setFrameData] = useState({});

  // Context variable
  const [storyData, setStoryData] = useState([]);

  const [fields, setFields] = useState([]);
	const [userId, setUserId] = useState("");
  
  useEffect(() => {
    fetch('/userStoryTemplate.json')
      .then(response => response.json())
      .then(data => {
        setStoryTemplate(data);
        setFrameData(data.frames[0]);
      });
  }, []);

  const setStoryDataFunc = (data) => {
    setStoryData(prev => {
      const index = prev.findIndex(item => item.target === data.target);
      if(index !== -1) {
        prev[index] = data;
        const a = prev.slice(0, index+1);
        return [...a];
      } else {
        return [...prev, data];
      }
    });
  };

  // console.log(storyData);

  const changeFrame = () => {
    if(storyTemplate.frames.length !== 0) {
      const index = storyTemplate.frames.findIndex(item => item.frameTemplateName === frameData.frameTemplateName);
      if(index+1 < storyTemplate.frames.length) {
        setPreviousFrameContext(frameData);
        setFrameData(storyTemplate.frames[index+1]);
      }
    }
  }

  // useEffect(() => {
  //   // if(storyTemplate.frames.length !== 0) {
  //   //   const index = storyTemplate.frames.findIndex(item => item.frameTemplateName === frameData.frameTemplateName);
  //   //   setPreviousFrameContext({ templateName: storyTemplate.frames[index].frameTemplateName, contextField: storyTemplate.frames[index].contextField });
  //   // }
  //   setPreviousFrameContext(frameData);
  // }, []);

  const [params, setParams] = useState({});
  useEffect(() => {
    if(frameData.params) {
      storyData.find(item => {
        if(Object.keys(item.result) === frameData.params) {
          setParams({
            [frameData.params]: item.result[frameData.params]
          });
        }
      });
    }
  }, [frameData]);

  return (
    <div>
      {
        storyTemplate.frames.length !== 0 && 
        <div className='userStory-page'>
          <h1 className='title'>{storyTemplate.title}</h1>
          <div>
            <div className='storyFrame-container'>
              <div className='opCodeSearch-container'>
                <h2 className='title'>{frameData.actionTitle}</h2>
                <div>
                  <OpCodeSearch setFields={setFields} setUserId={setUserId} templateName={frameData.frameTemplateName} previousFrameContext={previousFrameContext} />
                </div>
              </div>
              <div className='viewDetails-container'>
                <h2 className='title'>{frameData.viewDetailTitle}</h2>
                <ViewDetails data={{user_id: userId, fields: fields, target: frameData.frameTemplateName, contextField: frameData.contextField}} setStoryDataFunc={setStoryDataFunc} changeFrame={changeFrame} changeUrlParameter={changeUrlParameter} />
              </div>
            </div>
          </div>
        </div>
      }
    </div>
  )
}

export default UserStory