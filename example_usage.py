from client import RealtimeSubsecondGenerativeMediaStreamOrchestratorClient

def main():
    client = RealtimeSubsecondGenerativeMediaStreamOrchestratorClient()
    res = client.stream_realtime_diffusion_frames('webrtc://cam_node_hd', 60, 100)
    print('Stream Session: ' + res['stream_session_id'] + ' (' + str(res['rendered_fps']) + ' FPS)')
    print('Glass-to-Glass Latency: ' + str(res['end_to_end_glass_to_glass_latency_ms']) + 'ms (Target: <100ms)')
    print('WebRTC Active: ' + str(res['bidirectional_webrtc_stream_active']) + ' on ' + res['serverless_gpu_mesh_node'])

if __name__ == '__main__':
    main()
