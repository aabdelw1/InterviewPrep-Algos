// Using Fetch API with callbacks
function fetchDataWithCallback(url, callback) {
  fetch(url)
    .then(response => response.json())
    .then(data => callback(null, data))
    .catch(error => callback(error, null));
}

fetchDataWithCallback('https://api.example.com/data', (error, data) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('Data:', data);
  }
});

// Using Fetch API with promises
function fetchDataWithPromise(url) {
  return fetch(url)
    .then(response => response.json());
}

fetchDataWithPromise('https://api.example.com/data')
  .then(data => console.log('Data:', data))
  .catch(error => console.error('Error:', error));

// Using Fetch API with async/await
async function fetchDataWithAsyncAwait(url) {
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data;
  } catch (error) {
    throw new Error(error);
  }
}

(async () => {
  try {
    const data = await fetchDataWithAsyncAwait('https://api.example.com/data');
    console.log('Data:', data);
  } catch (error) {
    console.error('Error:', error);
  }
})();
