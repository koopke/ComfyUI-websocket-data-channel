from server import PromptServer
import torch

class WebSocketStringSenderNode:
    """
    A custom node to send a string message through WebSocket and handle UI integration,
    allowing for dynamic specification of message type and data.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "message_type": ("STRING", {"forceInput": True}),
                "message_data": ("STRING", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    FUNCTION = "send_message"
    OUTPUT_NODE = True
    CATEGORY = "Communication"

    def send_message(self, message_type, message_data):
        server = PromptServer.instance

        try:
            # Send the message using dynamic inputs for type and data
            server.send_sync(
                message_type,
                message_data
            )
            status_type = f"Type sent: {message_type}"
            status_data = f"Data sent: {message_data}"
        except Exception as e:
            # Error handling if the message fails to send
            status_type = f"Failed to send type: {message_type}, error: {str(e)}"
            status_data = f"Failed to send data: {message_data}, error: {str(e)}"

        # Return type and data as separate outputs for the UI
        return ({"ui": {"status_type": status_type, "status_data": status_data}, 
                 "result": (status_type, status_data)})

# Node registration (assuming there's a system to register custom nodes)
NODE_CLASS_MAPPINGS = {
    "WebSocketStringSender": WebSocketStringSenderNode
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "WebSocketStringSender": "WebSocket String Sender Node"
}
