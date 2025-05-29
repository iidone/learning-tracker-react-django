import React from 'react';
import { useEffect, useState } from 'react';

interface Users {
  id: number;
  username: string;
  name: string;
  last_name: string;
  created_at: string;
}

function App() {
  const [items, setItems] = useState<Users[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/users/')
      .then(response => response.json())
      .then(data => {
        setItems(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error:', error);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h1>Список элементов</h1>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            <h2>{item.username} </h2>
            <p>{item.name}</p>
            <p>{item.last_name}</p>
            <p>Создан {item.created_at}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;