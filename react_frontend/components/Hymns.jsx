import React, { useEffect, useState } from 'react';
import GetHymnForm from './GetHymnForm';
import api from '../api';

const HymnList = () => {
  const [hymns, setHymns] = useState([]);

  const fetchHymns = async () => {
    try {
      const response = await api.get('/hymns');
      setHymns(response.data.hymns);
    } catch (error) {
      console.error("Error fetching hymns", error);
    }
  };

  const addHymn = async (HymnNumber) => {
    try {
      await api.post('/hymns', { name: HymnNumber });
      fetchFruits();  // Refresh the list after adding a fruit
    } catch (error) {
      console.error("Error getting hymn", error);
    }
  };

  useEffect(() => {
    fetchHymns();
  }, []);

  return (
    <div>
      <h2>Hymns List</h2>
      <ul>
        {fruits.map((hymn, index) => (
          <li key={index}>{hymn.name}</li>
        ))}
      </ul>
      <GetHymnForm addFruit={addHymn} />
    </div>
  );
};

export default HymnList;