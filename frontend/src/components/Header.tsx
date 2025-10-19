import { Link } from "react-router-dom";
import styles from "./Header.module.css"; // CSS Module

function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.logo}>🛒 Amazon Clone</div>
      <nav className={styles.nav}>
        <Link to="/">Home</Link>
        <Link to="/login">Login</Link>
        <Link to="/register">Register</Link>
      </nav>
    </header>
  );
}

export default Header;
