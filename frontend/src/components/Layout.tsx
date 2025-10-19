import type { ReactNode } from "react";
import Header from "./Header";
import Footer from "./Footer";

type LayoutProps = {
  children: ReactNode;
};

function Layout({ children }: LayoutProps) {
  return (
    <>
      <Header />
      <main style={{ minHeight: "85vh" }}>{children}</main>
      <Footer />
    </>
  );
}

export default Layout;
