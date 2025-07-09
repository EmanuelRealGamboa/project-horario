import React, { useState } from 'react';

const daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
const timeSlots = ['08:00-10:00', '10:00-12:00', '12:00-14:00', '14:00-16:00'];

export default function TeacherAvailabilityForm() {
  const [availability, setAvailability] = useState({});

  const toggleSlot = (day, time) => {
    setAvailability(prev => {
      const current = prev[day] || [];
      return {
        ...prev,
        [day]: current.includes(time)
          ? current.filter(t => t !== time)
          : [...current, time]
      };
    });
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch('/api/teacher/availability/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + localStorage.getItem('token')
        },
        body: JSON.stringify({ availability })
      });

      if (response.ok) {
        alert('Disponibilidad enviada correctamente');
      } else {
        alert('Error al enviar disponibilidad');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="form-container">
      <h2>Selecciona tu disponibilidad</h2>
      {daysOfWeek.map(day => (
        <div key={day}>
          <h3>{day}</h3>
          {timeSlots.map(time => (
            <label key={time}>
              <input
                type="checkbox"
                checked={(availability[day] || []).includes(time)}
                onChange={() => toggleSlot(day, time)}
              />
              {time}
            </label>
          ))}
        </div>
      ))}
      <button onClick={handleSubmit}>Enviar disponibilidad</button>
    </div>
  );
}
