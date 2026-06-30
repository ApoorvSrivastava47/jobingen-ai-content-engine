import { useState } from "react";

import MainLayout from "./layout/MainLayout";

import Hero from "./components/Hero";
import TopicInput from "./components/TopicInput";
import WorkflowStatus from "./components/WorkflowStatus";
import StrategyCard from "./components/StrategyCard";
import ContentCard from "./components/ContentCard";
import ReviewCard from "./components/ReviewCard";
import Footer from "./components/Footer";
import EmptyState from "./components/EmptyState";

import "./App.css";

function App() {

  const [result, setResult] = useState(null);

  return (

    <MainLayout>

      <Hero />

      <TopicInput onGenerate={setResult} />

      <div className="top-grid">

        <StrategyCard strategy={result?.strategy} />

        <WorkflowStatus result={result} />

      </div>

      {
        result ? (
        <>
        <ContentCard content={result.content}/>

        <ReviewCard review={result.review}/>
        </>
        ):(
        <EmptyState/>
        )
        }
      <Footer />

    </MainLayout>

  );

}

export default App;