from expanse.console.commands.command import Command


class HelloCommand(Command):
    name = "hello"
    description = "Say hello to the world."

    def handle(self) -> int:
        self.line("Hello, <comment>World!</comment>")

        return 0
