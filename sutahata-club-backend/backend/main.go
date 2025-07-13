package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

func main() {
    r := gin.Default()

    // Serve frontend static files
    r.Static("/static", "./frontend")

    // Route: Home page
    r.GET("/", func(c *gin.Context) {
        c.File("./frontend/index.html")
    })

    // Route: Login page
    r.GET("/login", func(c *gin.Context) {
        c.File("./frontend/login.html")
    })

    // Placeholder API route
    r.GET("/api/ping", func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H{"message": "pong"})
    })

    r.Run() // default :8080
}
