document.querySelector("#btn").addEventListener("click", (e) => {
  e.preventDefault();

  const query = {
    text: document.getElementById("review_text").value,
  };
  document.cookie = `query=${query.text}`;
  (async () =>
    await fetch("http://127.0.0.1:5000/predict", {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => {
        document.querySelector(".app__classification").innerHTML = `<p>${
          query.text
        }</p><h1 class="${String(data.sentiment).toLowerCase()}">${
          data.sentiment
        }</h1>`;
      })
      .catch((error) => {
        console.log(error);
      }))();
});
