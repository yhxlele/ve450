// @material-ui/icons
import Dashboard from "@material-ui/icons/Dashboard";
import ContentPaste from "@material-ui/icons/ContentPaste";
// core components/views
import DashboardPage from "../App";
import TableList from "../monitor"
// import TableList from "";

const dashboardRoutes = [
  {
    path: "/dashboard",
    sidebarName: "Dashboard",
    navbarName: "Container Dashboard",
    icon: Dashboard,
    component: DashboardPage
  },
  {
    path: "/table",
    sidebarName: "Table List",
    navbarName: "Table List",
    icon: ContentPaste,
    component: TableList
  },
  { redirect: true, path: "/", to: "/dashboard", navbarName: "Redirect" }
];

export default dashboardRoutes;
