import { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import API from "../services/api";

function ChatBox() {

  const [query,setQuery]=useState("");
  const [messages,setMessages]=useState([]);
  const [loading, setLoading] = useState(false);

  const loadHistory = async () => {

    try {

      const res = await API.get("/chat/history");

      setMessages(res.data);

    } catch (err) {

      console.log(err);

    }

  };
  const messagesEndRef = useRef(null);

    useEffect(() => {
      messagesEndRef.current?.scrollIntoView({
        behavior: "smooth",
      });
    }, [messages, loading]);

    useEffect(() => {
      loadHistory();
    }, []);
    const sendMessage = async () => {
      if (!query.trim() || loading) return;

      const userQuery = query;
      setLoading(true);

      setMessages((prev) => [
        ...prev,
        {
          type: "user",
          text: userQuery,
        },
      ]);

      setQuery("");

      try {
          const res = await API.post("/chat/chat", {
          query: userQuery,
        });

        setMessages((prev) => [
          ...prev,
          {
            type: "bot",
            text: res.data.answer,
          },
        ]);
      } catch (err) {
        console.log(err);
      } finally {
        setLoading(false);
      }
    };

  return(

<div className="h-full flex flex-col overflow-hidden bg-white rounded-2xl shadow">

<div className="bg-gradient-to-r from-purple-700 to-violet-600 text-white px-5 py-4 text-lg font-semibold rounded-t-xl">

AI Assistant

</div>

<div className="flex-1 overflow-y-auto p-6 bg-gray-100">

  {messages.length === 0 && (
    <div className="flex h-full items-center justify-center text-center px-8 text-gray-500">
      <div>
        <h2 className="text-3xl font-semibold text-purple-700 mb-3">
          NASA AI Assistant
        </h2>

        <p>
          Ask about engine health, RUL prediction,
          maintenance recommendations,
          risk analysis or reports.
        </p>
      </div>
    </div>
  )}

{messages.map((msg,index)=>(

<div
key={index}
className={`mb-3 ${
msg.type==="user"
?"text-right":"text-left"
}`}
>

<div
className={`inline-block max-w-[80%] px-4 py-3 rounded-xl ${
msg.type==="user"
?"bg-purple-700 text-white"
:"bg-white border border-gray-200 shadow-sm text-gray-800"
}`}
>

{msg.type === "bot" ? (
  <ReactMarkdown>
    {msg.text}
  </ReactMarkdown>
) : (
  msg.text
)}

</div>
</div>

))}

{loading && (
  <div className="mb-3 text-left">
    <div className="inline-block bg-white border border-gray-200 shadow-sm rounded-xl px-4 py-3 text-gray-500 italic">
      AI is analysing...
    </div>
  </div>
)}

<div ref={messagesEndRef}></div>

</div>

<div className="border-t bg-white p-4 flex gap-3">

<input  disabled={loading}

className="flex-1 border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-purple-500"

value={query}

onChange={(e)=>setQuery(e.target.value)}

placeholder="Ask anything..."

onKeyDown={(e)=>{
if(e.key==="Enter" && !loading){
sendMessage();
}
}}

/>

<button
  onClick={sendMessage}
  disabled={loading}
  className={`px-6 rounded-xl font-medium text-white transition ${
    loading
      ? "bg-gray-400 cursor-not-allowed"
      : "bg-purple-700 hover:bg-purple-800"
  }`}
>
  {loading ? "Thinking..." : "Send"}
</button>

</div>

</div>

);

}

export default ChatBox;