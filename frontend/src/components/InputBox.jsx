import { useState } from "react";

function InputBox({ onSend }) {
  const [text, setText] = useState("");

  const handleSend = () => {
    if (!text.trim()) return;

    if (onSend) {
      onSend(text);
    }

    setText("");
  };

  return (
    <div className="flex gap-2 p-4">

      <input
        type="text"
        placeholder="Ask me something..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        className="flex-1 border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-purple-500"
      />

      <button
        onClick={handleSend}
        className="bg-purple-600 text-white px-5 rounded-lg hover:bg-purple-700"
      >
        Send
      </button>

    </div>
  );
}

export default InputBox;