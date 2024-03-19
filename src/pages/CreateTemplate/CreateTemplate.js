import React, { useEffect, useRef, useState } from 'react';
import './CreateTemplate.css';
import Modal from '../../components/Modal/Modal';

const CreateTemplate = () => {
	const [template, setTemplate] = useState({
			"templateName": "",
			"tableName": "",
			"searchComponent": {},
			"tableComponent": {},
	});

  const changeTemplate = (e) => {
    const { name, value } = e.target;
    setTemplate((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  
  // const [showSelectItem, setShowSelectItem] = useState(false);
  // const [addSearchItem, setAddSearchItem] = useState(false);
  // const menuRef = useRef();
  // // Close drop down menu when click outside
  // useEffect(() => {
  //   const handleOutsideClick = (event) => {
  //     if(menuRef.current && !menuRef.current.contains(event.target)) {
  //       setShowSelectItem(false);
  //     }
  //   };

  //   document.addEventListener('click', handleOutsideClick);

  //   return () => {
  //     document.removeEventListener('click', handleOutsideClick);
  //   }
  // });

  // const showSelectItemFunc = () => {
  //   setShowSelectItem(!showSelectItem);
  // }


  // const [tableComponent, setTableComponent] = useState({});
  // const addTableComponent = (type, dataType) => {
  //   console.log(type, dataType);
  //   setTemplate((prevState) => ({
  //     ...prevState,
  //     tableComponent: {
  //       fields: [
  //         {
  //           "key": "",
  //           "title": "",
  //           "size": "",
  //         }
  //       ]
  //     }
  //   }));
  // }

  return (
    <div>
			<div className='template'>
				<div className='template-section'>
						<h3>Template Name</h3>
            <div className='template-input'>
              <input 
                name='templateName' 
                type="text" 
                placeholder='Enter Template Name' 
                value={template.templateName || ""} 
                onChange={changeTemplate}
                className='input-box'
                />
              </div>
				</div>
				<div className='template-section'>
						<h3>Table Name</h3>
            <div className='template-input'>
              <input 
                name='tableName' 
                type="text" 
                placeholder='Enter Table Name' 
                value={template.tableName || ""} 
                onChange={changeTemplate} 
                className='input-box'
                />
            </div>
				</div>
				<div className='template-section'>
						<h3>Search Component</h3>
            <Modal />

            {/* <div className='add-container'  ref={menuRef}>
              <button className='add-button'  onClick={() => setAddSearchItem(!addSearchItem)}>+ Add</button>
              <div className={`${addSearchItem? '': 'hide'} select-item `} ref={menuRef}>
                <div className='list'>
                  <li onClick={() => {addTableComponent('text', 'string'); showSelectItemFunc();}} >Text</li>
                  <li onClick={() => {addTableComponent('email', 'string'); showSelectItemFunc();}} >Email</li>
                  <li onClick={() => {addTableComponent('number', 'number'); showSelectItemFunc();}} >Number</li>
                  <li onClick={() => {addTableComponent('radio', 'string'); showSelectItemFunc();}} >Radio</li>
                  <li onClick={() => {addTableComponent('dropdown', 'string'); showSelectItemFunc();}} >DropDown</li>
                </div>
              </div>
            </div> */}
				</div>
				<div className='template-section'>
				    <h3>Table Component</h3>
            {
              template.tableComponent.fields && template.tableComponent.fields.map((field, index) => 
              <div className='template-section'>
                <div className='template-input'>
                  <div>
                    <label>Key</label>
                    <input 
                      name='key' 
                      type="text" 
                      placeholder='Enter Key' 
                      value={field.key || ""} 
                      onChange={changeTemplate} 
                      className='input-box'
                      />
                  </div>
                  <div>
                    <label>Title</label>
                    <input 
                      name='title' 
                      type="text" 
                      placeholder='Enter Title' 
                      value={field.title || ""} 
                      onChange={changeTemplate} 
                      className='input-box'
                      />
                  </div>
                  <div>
                    <label>Size</label>
                    <input 
                      name='size' 
                      type="text" 
                      placeholder='Enter Size' 
                      value={field.size || ""} 
                      onChange={changeTemplate} 
                      className='input-box'
                      />
                  </div>
                </div>
              </div>
               )
            }
				</div>
				<div className='template-section'>
						<h3>Form Component</h3>
				</div>
				<div className='template-section'>
						<h3>View Details Component</h3>
				</div>
			</div>
			<div  className='template'>
				<div>
          {
            JSON.stringify(template, null, 2)
          }
				</div>
			</div>
    </div>
  )
}

export default CreateTemplate