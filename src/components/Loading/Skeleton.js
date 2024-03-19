import React from 'react';
import './Skeleton.css'; // Import your styles

const Skeleton = () => {
  return (
    <div className="skeleton-container">
      <div className="skeleton-content" style={{width: '100%'}}></div>
      <div className="skeleton-content" style={{width: '80%'}}></div>
      <div className="skeleton-content" style={{width: '49%'}}></div>
      <div className="skeleton-content" style={{width: '49%'}}></div>
      <div className="skeleton-content" style={{width: '60%'}}></div>
      <br />
      <div className="skeleton-content" style={{width: '60%'}}></div>
    </div>
  );
};

export default Skeleton;
