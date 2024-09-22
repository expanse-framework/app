from expanse.testing.command_tester import CommandTester


def test_hello(command_tester: CommandTester) -> None:
    command = command_tester.command("hello")

    return_code: int = command.run()

    assert return_code == 0
    assert command.output.fetch() == "Hello, World!\n"
