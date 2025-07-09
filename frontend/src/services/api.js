export const API_BASE = 'http://localhost:8000/api'; // Ajusta si cambia la URL

export const postAvailability = async (data) => {
  const token = localStorage.getItem('token');
  const res = await fetch(`${API_BASE}/teacher/availability/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    },
    body: JSON.stringify(data)
  });
  return res.json();
};
