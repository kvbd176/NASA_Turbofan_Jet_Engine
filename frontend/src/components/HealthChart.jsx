import { useEffect, useState } from "react";
import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
} from "recharts";

import API from "../services/api";

const COLORS = [
  "#8b5cf6",
  "#c4b5fd",
  "#e5e7eb",
];
const [loading,setLoading] = useState(true);
const [error,setError] = useState(false);

function HealthChart() {
  const [data,setData]=useState([]);
  useEffect(()=>{
    async function load(){
 try{
  const res = await API.get(
    "/analytics/health-distribution"
  );
  const chartData = Object.entries(res.data)
  .map(([name,value])=>({
      name,
      value
  }));
  setData(chartData);
 }catch(err){
  console.error(err);
  setError(true);
 }
 finally{
  setLoading(false);
 }
}
  load();
  },[]);
  
  return(
    <div className="bg-white rounded-xl border p-5">
      <h2 className="font-semibold mb-4">
        Health Status
      </h2>
      <div className="h-56">
        <ResponsiveContainer>
          <PieChart>
            <Pie
              data={data}
              dataKey="value"
              nameKey="name"
              innerRadius={55}
              outerRadius={80}
            >
              {
                data.map((entry,index)=>
                  <Cell
                    key={index}
                    fill={COLORS[index]}
                  />
                )
              }
            </Pie>
            <Tooltip/>
          </PieChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default HealthChart;
