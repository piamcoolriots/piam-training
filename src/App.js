import './App.css'; 
import { Route, Routes } from "react-router-dom";
import UserStory from './pages/UserStory/UserStory';
import OpCodeSearch from './pages/OpCodeSearch/OpCodeSearch';
import OpCodeCreate from './pages/OpCodeCreate/OpCodeCreate';
import { Toaster } from "react-hot-toast";

function App() {
	return (
		<div>
			<Routes>
				<Route path="/" element={<h2>Home Page</h2>} />
				<Route path="/UserStory" element={<UserStory />} />
				<Route path="/OpCodeSearch" element={<OpCodeSearch />} />
				<Route path="/OpCodeCreate" element={<OpCodeCreate />} />
				<Route path="*" element={<h2>404 Not Found</h2>} />
			</Routes>
			<Toaster />
		</div>
	);
}

export default App;