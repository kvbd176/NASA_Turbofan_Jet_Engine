import { motion } from "framer-motion";
import { Cpu, Activity, ShieldCheck, Bot, GaugeCircle } from "lucide-react";
import { useEffect, useState } from "react";

const messages = [
  "Monitoring Engine Health...",
  "Analyzing Sensor Data...",
  "Predicting Remaining Useful Life...",
  "Detecting Fault Patterns...",
  "Generating Maintenance Insights..."
];

function AuthHero() {
  const [text, setText] = useState(messages[0]);

  useEffect(() => {
    let index = 0;

    const interval = setInterval(() => {
      index = (index + 1) % messages.length;
      setText(messages[index]);
    }, 2500);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="hidden lg:flex w-1/2 bg-gradient-to-br from-purple-800 via-purple-700 to-purple-900 text-white p-14 flex-col justify-center overflow-hidden">

      <h1 className="text-5xl font-bold mb-4">
        NASA Turbofan
        <br />
        Predictive Maintenance
      </h1>

      <p className="text-purple-100 mb-10 text-lg">
        AI-powered Engine Health Monitoring Platform
      </p>

      <div className="space-y-5">

        <div className="flex items-center gap-3">
          <Activity />
          <span>Health Monitoring</span>
        </div>

        <div className="flex items-center gap-3">
          <GaugeCircle />
          <span>RUL Prediction</span>
        </div>

        <div className="flex items-center gap-3">
          <ShieldCheck />
          <span>Risk Assessment</span>
        </div>

        <div className="flex items-center gap-3">
          <Bot />
          <span>AI Maintenance Assistant</span>
        </div>

      </div>

      <motion.p
        key={text}
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="mt-14 text-xl font-semibold text-purple-100"
      >
        {text}
      </motion.p>

      <div className="flex gap-10 mt-12">

        <div>
          <h2 className="text-3xl font-bold">98.9%</h2>
          <p className="text-purple-200">Prediction Accuracy</p>
        </div>

        <div>
          <h2 className="text-3xl font-bold">500+</h2>
          <p className="text-purple-200">Engines Monitored</p>
        </div>

      </div>

    </div>
  );
}

export default AuthHero;