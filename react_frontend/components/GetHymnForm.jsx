import React, { useState } from 'react';

const GetHymnForm = ({ addFruit }) => {
  const [fruitName, setFruitName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (fruitName) {
      addFruit(fruitName);
      setFruitName('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={hymnNumber}
        onChange={(e) => setFruitName(e.target.value)}
        placeholder="Enter Hymn Number"
      />
      <button type="submit">Hymn Number</button>
    </form>
  );
};

export default GetHymnForm;