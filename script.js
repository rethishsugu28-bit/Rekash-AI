async function send() {
  const input = document.getElementById("input");
  const chat = document.getElementById("chat");
  const text = input.value.trim();

  if (!text) return;

  chat.innerHTML += `<div class="user">You: ${text}</div>`;
  input.value = "";
  chat.scrollTop = chat.scrollHeight;

  try {
    const res = await fetch("http://127.0.0.1:5000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: text })
    });

    const data = await res.json();
    chat.innerHTML += `<div class="bot">Rekash: ${data.answer}</div>`;
    chat.scrollTop = chat.scrollHeight;

  } catch (error) {
    chat.innerHTML += `<div class="bot">⚠️ Backend not running</div>`;
  }
}
