function timeToSeconds(time) {
  const [minutes, seconds] = time.split(':').map(Number);
  return minutes * 60 + seconds;
}

function secondsToTime(seconds) {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = seconds % 60;
  return `${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
}

function solution(video_len, pos, op_start, op_end, commands) {
  const videoLenSeconds = timeToSeconds(video_len);
  const opStartSeconds = timeToSeconds(op_start);
  const opEndSeconds = timeToSeconds(op_end);
  let currentPos = timeToSeconds(pos);

  for (const cmd of commands) {
    if (currentPos >= opStartSeconds && currentPos <= opEndSeconds) {
      currentPos = opEndSeconds;
    }

    if (cmd === 'next') {
      if (currentPos + 10 >= videoLenSeconds) {
        currentPos = videoLenSeconds;
      } else {
        currentPos += 10;
      }
    } else {
      // prev
      if (currentPos < 10) {
        currentPos = 0;
      } else {
        currentPos -= 10;
      }
    }

    if (currentPos >= opStartSeconds && currentPos <= opEndSeconds) {
      currentPos = opEndSeconds;
    }
  }

  return secondsToTime(currentPos);
}

console.log(solution('34:33', '13:00', '00:55', '02:55', ['next', 'prev']));

/**
 * prev - 10초 전으로 이동
 * * 남은 시간이 10초 미만일 경우, 영상의 처음 위치로 이동 (00:00)
 * next - 10초 후로 이동
 * * 남은 시간이 10초 미만일 경우, 영상의 마지막 위치로 이동
 * 오프닝 건너뛰기 (op_start <= 현재 재생위치 <= op_end)
 * 숫자가 한 자리일 경우, 0으로 두 자리 맞추기
 *
 */
