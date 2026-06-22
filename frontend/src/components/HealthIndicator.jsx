import React, { useState, useEffect } from 'react';
import './HealthIndicator.css';

const HealthIndicator = () => {
  const [status, setStatus] = useState('loading'); // 'ok', 'error', 'loading'

  useEffect(() => {
    const fetchHealth = async () => {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 5000);
        
        const response = await fetch('http://localhost:8000/api/health', {
          signal: controller.signal
        });
        clearTimeout(timeoutId);

        if (response.ok) {
          const data = await response.json();
          if (data.status === 'ok') {
            setStatus('ok');
          } else {
            setStatus('error');
          }
        } else {
          setStatus('error');
        }
      } catch (err) {
        setStatus('error');
      }
    };

    fetchHealth();
    const interval = setInterval(fetchHealth, 10000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className={`health-indicator ${status}`}>
      <span className="pulse-dot"></span>
      <span className="status-text">
        {status === 'ok' ? 'System Operational' : status === 'error' ? 'System Error' : 'Checking...'}
      </span>
    </div>
  );
};

export default HealthIndicator;
