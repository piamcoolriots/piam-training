import React, { useEffect, useRef, useState } from 'react';
import { BiChevronDown, BiSearch } from 'react-icons/bi';
import './DropDown.css';
import { SERVER1 } from '../../utils/server';
import capitalizeFirstCharWord from '../../utils/CapitalizeFirstCharWord';

const DropDown = ({item, formData, data, handleInputChange }) => {
  const [showDropDown, setShowDropDown] = useState(false);
  const [search, setSearch] = useState('');

  const [values, setValues] = useState([]);
  const [dependOnValue, setDependOnValue] = useState('');

  const menuRef = useRef();

  // Toggle drop down menu
  const toggleDropDownMenu = () => {
    if(item.dependOn) {
      if(formData[item.dependOn]) {
        setShowDropDown(!showDropDown);
      }
      else {
        setShowDropDown(false);
      }
    }
    else {
      setShowDropDown(!showDropDown);
    }
  }

  // Close drop down menu when click outside
  useEffect(() => {
    const handleOutsideClick = (event) => {
      if(menuRef.current && !menuRef.current.contains(event.target)) {
        setShowDropDown(false);
      }
    };

    document.addEventListener('click', handleOutsideClick);

    return () => {
      document.removeEventListener('click', handleOutsideClick);
    }
  });

  // clear search when close drop down menu
  useEffect(() => {
    if(showDropDown === false) {
      setSearch('');
    }
  }, [showDropDown]);

  // Fetch values from the SERVER1
  useEffect(() => {
    if(item.dependOn) {
      if(formData[item.dependOn] && item.lutApi) {
        fetch(`${SERVER1}${item.lutApi}/${formData[item.dependOn]}`)
        .then(res => res.json())
        .then(data => {
          setValues(data);
          if(formData[item.dependOn] !== dependOnValue) {
            delete formData[item.key];
          }
          setDependOnValue(formData[item.dependOn]);
        })
      }
    }
    else {
      if(item.values) {
        setValues(item.values);
      }
      else {
        fetch(`${SERVER1}${item.lutApi}`)
        .then(res => res.json())
        .then(data => {
          setValues(data);
        })
      }
    }
  }, [dependOnValue, formData, item.dependOn, item.key, item.lutApi, item.values]);

  // Filter values when search
  useEffect(() => {
    if(item.values) {
      if(search === '') {
        setValues(item.values);
      }
      else {
        const filteredValues = item.values.filter(value => value.toLowerCase().includes(search.toLowerCase()));
        setValues(filteredValues);
      }
    }
    else if (item.dependOn) {
      if(search === '') {
        setValues(values);
      }
      else {
        const filteredValues = values.filter(value => value.toLowerCase().includes(search.toLowerCase()));
        setValues(filteredValues);
      }
    }
    else {
      fetch(`${SERVER1}${item.lutApi}/${capitalizeFirstCharWord(search)}`)
      .then(res => res.json())
      .then(data => {
        setValues(data);
      })
    }
  }, [search]);

  const handleSearchChange = (e) => {
    const { value } = e.target;
    setSearch(value);
  };

  return (
    <div ref={menuRef} className='drop-down-container' style={{width: `${item?.width ? item?.width : '100%'}`}}>
      <div className='drop-down-box' 
        style={{backgroundColor: `${item.dependOn ? (formData[item.dependOn]? "" : "#ccc5" ) : ""}`}}
        onClick={toggleDropDownMenu} 
      >
        {
          formData? 
          <>{(formData[item.key] === undefined) ? <div>{item.placeholder}</div> :" "}</>:
          <>{(data[item.key] === undefined) ? <div>{item.placeholder}</div> :" "}</>
        }
        {
          (formData) ? 
          <div style={{color: 'black'}}>{formData[item.key]}</div>
          :
          // item.placeholder
          <>
            {(data !== undefined) ? <div style={{color: "black"}}>{data[item.key]}</div>: item.placeholder }
          </>
        }
        
        {
          showDropDown === false ? <BiChevronDown className='drop-down-icon' /> : <BiChevronDown className='drop-down-icon' style={{transform: 'rotate(180deg)'}} />
        }
      </div>
      { 
        showDropDown === true &&
        <div className='drop-down-menu-option-container'>
          <div className='drop-down-menu'>
            {
              item.searchable &&
              <div className='search'>
                <BiSearch />
                <input 
                  type='text'
                  placeholder='Search'
                  value={search || ''}
                  onChange={handleSearchChange}
                />
              </div>
            }
            <div className='options'>
              { values && 
                values.map((value, index) => 
                  <div key={index} 
                    className='option' 
                    onClick={() => {
                      handleInputChange({target: {name: item.key, value: value}});
                      setShowDropDown(false);
                    }}
                  >{value}</div>
                )
              }
            </div>
          </div>
        </div>
      }
    </div>
  )
}

export default DropDown