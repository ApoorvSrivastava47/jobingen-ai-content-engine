import "../styles/Layout.css";

function MainLayout({ children }) {
  return (
    <div className="layout">
      {children}
    </div>
  );
}

export default MainLayout;