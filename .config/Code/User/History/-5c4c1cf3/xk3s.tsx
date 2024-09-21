"use client";

import React from "react";
const Grid = dynamic(() => import("@/components/Grid"));
const Hero = dynamic(() => import("@/components/Hero"));
const Projects = dynamic(() => import("@/components/Projects"), {
  ssr: false,
});
const Experience = dynamic(() => import("@/components/Experience"));
import { FloatingNav } from "@/components/ui/FloatingNavbar";
import { navItems } from "@/data";
const Publications = dynamic(() => import("@/components/Publications"));
const Footer = dynamic(() => import("@/components/Footer"));
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
