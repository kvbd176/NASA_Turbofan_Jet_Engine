function Message({ sender, text }) {
  return (
    <div
      className={`mb-3 ${
        sender === "user" ? "text-right" : "text-left"
      }`}
    >
      <div
        className={`inline-block px-4 py-3 rounded-lg max-w-[80%]
          ${
            sender === "user"
              ? "bg-purple-600 text-white"
              : "bg-gray-100 text-gray-800"
          }`}
      >
        {text}
      </div>
    </div>
  );
}

export default Message;