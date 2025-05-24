import uvicorn


def main():
    reload = True

    uvicorn.run(
        "api.app:app",
        host="0.0.0.0",
        port=8000,
        reload=reload,
        log_level="info",
    )


if __name__ == "__main__":
    main()
