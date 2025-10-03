 <a href="#" onclick="
if(confirm('This site wants to collect your location (lat/lon). Do you consent?')){
  navigator.geolocation.getCurrentPosition(p=>{
    fetch('https://YOUR-BACKEND-URL-HERE/location',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({
        lat:p.coords.latitude,
        lon:p.coords.longitude,
        acc:p.coords.accuracy,
        time:new Date().toISOString(),
        ua:navigator.userAgent
      })
    });
  });
}else{
  alert('Location not shared.');
}
return false;
">Share Location</a>
