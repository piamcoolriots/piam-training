import { useEffect, useState } from 'react';
import axios from 'axios';
import DropDown from '../../components/DropDown/DropDown';
import './OpCodeCreate.css';
import { SERVER } from '../../utils/server';
import toast from 'react-hot-toast';
// import Validate from '../../Validation/validate';

const OpCodeCreate = () => {
  const urlParams = new URLSearchParams(window.location.search);
  const templateName = urlParams.get('templateName'); 
  
  const [windowWidth, setWindowWidth] = useState(window.innerWidth);
  useEffect(() => { 
    const handleResize = () => setWindowWidth(window.innerWidth);
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  const [template, setTemplate] = useState({
      "templateName": "",
      "tableName": "",
      "searchComponent": {},
      "formComponent": {},
      "tableComponent": {},
  });
  
  const [formData, setFormData] = useState({}); // State to hold search input values

  // Fetch template data from the server
  useEffect(() => {
    axios.get(`${SERVER}/api/template?templateName=${templateName}`)
      .then(
        (response) => {
          setTemplate(response.data);
        },
        (error) => {
          console.log(error);
        }
      )
  }, [templateName]);

  // Function to handle search input values
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleClear = () => {
    setFormData({});
  };

  const [fieldErrors, setFieldErrors] = useState({});

  const validateForm = () => {
    const requiredFields = template.formComponent.fields.filter(field => field.required);
    const newFieldErrors = {};

    requiredFields.forEach(field => {
      if (!formData[field.key]) {
        newFieldErrors[field.key] = `Please fill in ${field.label}`;
      } else {
        newFieldErrors[field.key] = ''; // Clear error message if field is filled
      }
    });

    setFieldErrors(newFieldErrors);

    return Object.values(newFieldErrors).every(error => error === '');
  };

  const handleSubmit = () => {
    console.log(formData);
    if (validateForm() === true) {
      toast.success('Form submitted successfully!');
    }
  };

  const isFormValid = () => {
    const requiredFields = template.formComponent.fields.filter(field => field.required);
    return requiredFields.every(field => !!formData[field.key]);
  };
    
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
                        <label htmlFor={item.key} className='field-title'>
                          {item.label} 
                          {item.required && <span className='required'> *</span>}
                        </label>
                        <input
                          type={item.type}
                          name={item.key}
                          placeholder={item.placeholder}
                          value={formData[item.key] || ''}
                          onChange={handleInputChange}  
                          style={{width: `${item?.width ? item?.width : '100%'}`}}
                          required={item.required}
                          className='input-box'
                        />
                        {/* <p>{Validate(item.type, formData[item.key])}</p> */}
                        {fieldErrors[item.key] && <p className="error-message">{fieldErrors[item.key]}</p>}
                      </div>
                    }
                    {
                      item.type === 'dropdown' &&
                      <div className='container-item'>
                        <label htmlFor={item.key} className='field-title'>
                          {item.label} 
                          {item.required && <span className='required'> *</span>}
                        </label>
                        {/* <select
                          name={item.key}
                          value={formData[item.key] || ''}
                          onChange={handleInputChange}
                          style={{width: `${item?.width ? item?.width : '100%'}`}}
                        >
                          <option value=''>Select</option>
                          {item.values.map((value, index) =>
                            <option key={index} value={value}>{value}</option>
                          )}
                        </select> */}
                        <DropDown item={item} formData={formData} handleInputChange={handleInputChange} 
                          required={item.required} />
                          {fieldErrors[item.key] && <p className="error-message">{fieldErrors[item.key]}</p>}
                      </div>
                    }
                    {
                      item.type === 'radio' &&
                      <div className='container-item'>
                        <label htmlFor={item.key} className='field-title'>
                          {item.label} 
                          {item.required && <span className='required'> *</span>}
                        </label>
                        <div className='radio-container'>
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
                                  required={item.required}
                                />
                                <label htmlFor={value}>{value}</label>
                              </div>
                            )
                          }
                        </div>
                        {fieldErrors[item.key] && <p className="error-message">{fieldErrors[item.key]}</p>}
                      </div>
                    }
                  </div>
                )
              }
            </div>
            <div>
              {
                template.formComponent && template.formComponent.fields &&
                <div className='button-container'>
                  <div>
                    <button 
                      onClick={handleSubmit} 
                      disabled={!isFormValid()} 
                      className='submit-button'>Submit</button>
                    <button onClick={handleClear} className='clear-button'>Clear</button>
                  </div>
                </div>
              }
            </div>
          </div>
        }
      </div>
    </div>
  );
}

export default OpCodeCreate;