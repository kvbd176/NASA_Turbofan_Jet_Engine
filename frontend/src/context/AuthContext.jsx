import { createContext, useContext, useState, useEffect } from "react";
import api from "../services/api";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {

    const [user, setUser] = useState(
        JSON.parse(localStorage.getItem("user")) || null
    );

    useEffect(() => {

        const savedUser = localStorage.getItem("user");

        if (savedUser) {
            setUser(JSON.parse(savedUser));
        }

    }, []);

    const login = async (email, password) => {

        const form = new URLSearchParams();

        form.append("username", email);
        form.append("password", password);

        const response = await api.post(
            "/auth/login",
            form,
            {
                headers: {
                    "Content-Type":
                        "application/x-www-form-urlencoded"
                }
            }
        );

        localStorage.setItem(
            "token",
            response.data.access_token
        );

        localStorage.setItem(
            "user",
            JSON.stringify(response.data.user)
        );

        setUser(response.data.user);

        return response;
    };

    const register = async (username, email, password) => {

        return await api.post(
            "/auth/register",
            {
                username,
                email,
                password
            }
        );
    };

    const logout = () => {

        localStorage.removeItem("token");
        localStorage.removeItem("user");

        setUser(null);

        window.location.href = "/login";
    };

    return (

        <AuthContext.Provider
            value={{
                user,
                login,
                logout,
                register
            }}
        >

            {children}

        </AuthContext.Provider>

    );

};

export const useAuth = () => useContext(AuthContext);