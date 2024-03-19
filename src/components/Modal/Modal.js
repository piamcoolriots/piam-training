import { useEffect } from 'react';
import './Modal.css';

export const Modal = ({ open, onClose, children }) => {
  useEffect(() => {
    const handleOutsideClick = (e) => {
      if (open && e.target.classList.contains('modal')) {
        onClose();
      }
    };

    document.addEventListener('mousedown', handleOutsideClick);

    return () => {
      document.removeEventListener('mousedown', handleOutsideClick);
    };
  }, [open, onClose]);

  useEffect(() => {
    if (open) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'auto';
    }

    return () => {
      document.body.style.overflow = 'auto';
    };
  }, [open]);

  return (
    <div>
      {open && (
        <div className="modal">
          <div className='modal-content'>
            <div className='modal-header'>
              <div></div>
              <button className='close' onClick={onClose}>X</button>
            </div>
            <div className='modal-body'>
              {children}
            </div>
            <div className='modal-footer'>
              <button className='close' onClick={onClose}>Close</button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}