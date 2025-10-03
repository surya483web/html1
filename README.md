 <!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Get Location (consent required)</title>
  <style>
    body { font-family: system-ui, Arial; padding: 2rem; }
    a.location-link { display:inline-block; padding: .5rem 1rem; background:#007BFF; color:white; text-decoration:none; border-radius:6px; }
    .status { margin-top:1rem; color:#333; }
  </style>
</head>
<body>
  <h1>Share your location (consent required)</h1>
  <p>Click the link below to share your approximate location with the site owner. You will be prompted to allow location sharing in your browser.</p>

  <!-- Replace data-endpoint with your webhook/Apps Script URL -->
  <a href="#" class="location-link" id="shareLocationBtn" data-endpoint="https://YOUR_ENDPOINT_URL_HERE">Share location</a>

  <div class="status" id="status"></div>

  <script>
    const btn = document.getElementById('shareLocationBtn');
    const status = document.getElementById('status');

    btn.addEventListener('click', async (e) => {
      e.preventDefault();
      const endpoint = btn.dataset.endpoint;
      if (!endpoint) {
        status.textContent = 'Error: no endpoint configured.';
        return;
      }

      // Show an explicit consent dialog (custom). Do NOT auto-get location.
      const consent = confirm(
        'This site would like to collect your device location (latitude & longitude) and timestamp. ' +
        'This is only sent to the site owner. Do you consent?'
      );
      if (!consent) {
        status.textContent = 'You declined consent. Location not shared.';
        return;
      }

      // Check browser support
      if (!navigator.geolocation) {
        status.textContent = 'Geolocation API not supported by your browser.';
        return;
      }

      status.textContent = 'Requesting location — please allow the browser prompt...';

      // Ask for highAccuracy false to reduce battery/privacy if desired.
      navigator.geolocation.getCurrentPosition(async (pos) => {
        const payload = {
          lat: pos.coords.latitude,
          lon: pos.coords.longitude,
          accuracy_m: pos.coords.accuracy,
          timestampISO: new Date(pos.timestamp).toISOString(),
          userAgent: navigator.userAgent,
          page: location.href
        };

        status.textContent = 'Location obtained. Sending to server...';

        try {
          const resp = await fetch(endpoint, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
          });

          if (!resp.ok) {
            const text = await resp.text().catch(()=>'');
            status.textContent = 'Failed to send: ' + resp.status + ' ' + resp.statusText + ' ' + text;
          } else {
            status.textContent = 'Location sent successfully. Thank you!';
          }
        } catch (err) {
          status.textContent = 'Error sending location: ' + err.message;
          console.error(err);
        }
      }, (err) => {
        // geolocation error callback
        status.textContent = 'Location error: ' + (err.message || err.code);
      }, {
        enableHighAccuracy: false,
        timeout: 15000,
        maximumAge: 0
      });
    });
  </script>
</body>
</html>
