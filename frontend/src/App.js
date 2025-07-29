import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [contacts, setContacts] = useState([]);
  const [form, setForm] = useState({ name: '', email: '', phone: '' });

  useEffect(() => {
    axios.get('http://localhost:5000/contacts')
      .then(res => setContacts(res.data));
  }, []);

  const addContact = () => {
    axios.post('http://localhost:5000/contacts', form)
      .then(() => window.location.reload());
  };

  const deleteContact = (id) => {
    axios.delete(`http://localhost:5000/contacts/${id}`)
      .then(() => window.location.reload());
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Contact Book</h1>
      <input placeholder="Name" onChange={e => setForm({ ...form, name: e.target.value })} />
      <input placeholder="Email" onChange={e => setForm({ ...form, email: e.target.value })} />
      <input placeholder="Phone" onChange={e => setForm({ ...form, phone: e.target.value })} />
      <button onClick={addContact}>Add Contact</button>
      <ul>
        {contacts.map((c, i) => (
          <li key={i}>
            {c.name} | {c.email} | {c.phone} <button onClick={() => deleteContact(c.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;


