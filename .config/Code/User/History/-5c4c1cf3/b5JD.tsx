"use client";

import React from "react";
import Grid from "@/components/Grid";
// import Hero from "@/components/Hero";
const Hero = dynamic(() => import("@/components/Hero"));
const Projects = dynamic(() => import("@/components/Projects"), {
  ssr: false,
});
import Experience from "@/components/Experience";
import { FloatingNav } from "@/components/ui/FloatingNavbar";
import { navItems } from "@/data";
import Publications from "@/components/Publications";
import Footer from "@/components/Footer";
import Resume from "@/components/Resume";
import dynamic from "next/dynamic";


export default function Home() {
  return (
    <main className="relative bg-black-100 flex justify-center items-center flex-col mx-auto sm:px-10 px-5 overflow-clip">
      <div className="max-w-7xl w-full">
        <FloatingNav navItems={navItems} />
        <Hero />
        <Grid />
        <Projects/>
        {/* <Publications /> */}
        <Experience />
        {/* <Resume /> */}
        <Footer />
      </div>
    </main>
  );
}
