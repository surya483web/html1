<!doctype html>
<html>
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Share Location (consent)</title></head>
<body>
  <h2>Share Location (consent required)</h2>
  <p>This page will ask permission to share your location. It will only send the coordinates to the site owner.</p>

<script>
(async function autoRequestAndSend(){
  // Show explicit consent prompt before any geolocation call
  const consent = confirm(
    'This site requests permission to read your device location (latitude & longitude). ' +
    'If you agree, your location will be sent to the site owner and stored locally on their machine. ' +
    'Do you consent?'
  );
  if(!consent){
    console.log('User declined consent.');
    return;
  }

  if(!navigator.geolocation){
    alert('Geolocation not supported by your browser.');
    return;
  }

  // Request location
  navigator.geolocation.getCurrentPosition(async (pos) => {
    const payload = {
      lat: pos.coords.latitude,
      lon: pos.coords.longitude,
      accuracy_m: pos.coords.accuracy,
      timestampISO: new Date(pos.timestamp).toISOString(),
      page: location.href,
      userAgent: navigator.userAgent
    };

    try {
      // Send to local backend - change URL if different
      const resp = await fetch('http://localhost:3000/location', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
      });
      if(!resp.ok) {
        console.error('Failed to send location:', resp.status, resp.statusText);
      } else {
        console.log('Location sent successfully.');
      }
    } catch (err) {
      console.error('Error sending location:', err);
    }
  }, (err) => {
    console.error('Geolocation error:', err);
  }, {
    enableHighAccuracy: false,
    timeout: 15000,
    maximumAge: 0
  });
})();
</script>
</body>
</html>
