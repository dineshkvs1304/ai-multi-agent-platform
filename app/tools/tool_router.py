from app.tools.calculator import calculate_growth


def run_tool(tool_name, args):

    if tool_name == "calculate_growth":

        return calculate_growth(
            args["old"],
            args["new"]
        )

    return None