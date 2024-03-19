import React from 'react';
import './Pagination.css';

const Pagination = ({ currentPage, totalPages, onPageChange }) => {
  const isFirstPage = currentPage === 1;
  const isLastPage = currentPage === totalPages;

  // Calculate the range of pages to display (5 pages total)
  const pageRange = Math.min(totalPages, 5);

  // Calculate the starting and ending page numbers for the pagination
  let startPage = Math.max(currentPage - Math.floor(pageRange / 2), 1);
  let endPage = startPage + pageRange - 1;

  if (endPage > totalPages) {
    endPage = totalPages;
    startPage = Math.max(endPage - pageRange + 1, 1);
  }

  const pageNumbers = [];
  for (let i = startPage; i <= endPage; i++) {
    pageNumbers.push(i);
  }

  return (
    <div className='pagination-space'>
      <button
        onClick={() => onPageChange(1)}
        disabled={isFirstPage}
        className={isFirstPage ? 'hide' : 'disabled'}
      >
        First
      </button>
      <button
        onClick={() => onPageChange(currentPage - 1)}
        disabled={isFirstPage}
        className={isFirstPage ? 'hide' : 'normal'}
      >
        {'<'}
      </button>
      {pageNumbers.map((page) => (
        <button
          key={page}
          onClick={() => onPageChange(page)}
          className={page === currentPage ? 'button-color-black' : 'button-color-white'}
        >
          {page}
        </button>
      ))}
      <button
        onClick={() => onPageChange(currentPage + 1)}
        disabled={isLastPage}
        className={isLastPage ? 'hide' : 'normal'}
      >
        {'>'}
      </button>
      <button
        onClick={() => onPageChange(totalPages)}
        disabled={isLastPage}
        className={isLastPage ? 'hide' : 'disabled'}
      >
        Last
      </button>
    </div>
  );
};

export default Pagination;
