"""Entry-point for the application."""
from cli.command_handler import CommandHandler
from cli.command_output import CommandResultStatus


def main() -> None:
    """Entry-point for the application."""
    result = CommandHandler().handle()
    if result.status != CommandResultStatus.SUCCESS:
        print(result.message)


if __name__ == "__main__":
    main()
