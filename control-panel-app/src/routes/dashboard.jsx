// @material-ui/icons
import Dashboard from "@material-ui/icons/Dashboard";
import ContentPaste from "@material-ui/icons/ContentPaste";
import Description from "@material-ui/icons/Description";
// core components/views
import DashboardPage from "../App";
import TableList from "../monitor";
import Result from "../Result"
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
  {
    path: "/result",
    sidebarName: "Results",
    navbarName: "Results",
    icon: Description,
    component: Result
  },
  { redirect: true, path: "/", to: "/dashboard", navbarName: "Redirect" }
];

export default dashboardRoutes;
