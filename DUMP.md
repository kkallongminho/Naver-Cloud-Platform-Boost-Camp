 1. DataTeleporter
  - DataTeleporter 한 대당 100TB의 저장용량을 가지며, 내부적으로 디스크 문제가 최소화될 수 있도록 설계
  - 별도의 요청이 없다면 DataTeleporter는 최초 대여 후 90일 이내에 네이버 클라우드 플랫폼으로 반환되어야 합니다
  - DataTeleporter는 고객이 신청한 암호화 키로 256비트 암호화되며, 암호키는 장치 내 그 어디에도 저장되지 않습니다.
  - Linux Server는NFS, Windows Server는 CIFS 공유 파일시스템으로 연결(mount)할 수 있습니다

 2. NAS
  - NAS는 임계치 설정에 따른 이벤트 알림 기능을 제공한다
  - NAS는 일정한 스케줄에 따라 자동 스냅샷을 완성한다.
  - NAS는 리눅스 서버에서 공유가능한 NFS 프로토콜을 제공한다.
  - 네이버클라우드플랫폼에서는 NAS 생성 시 마운트포인트 정보를 제공한다.

 3. 베어메탈
  - 4가지 스펙을 제공하고 있다.
  - OS로Oracle Linux도 제공한다.
  - 디스크 구성시 RAID 방식을 선택할 수 있다. 
  - 내 서버 이미지, 스탭샷, 추가 스토리지 기능은 제공하지 않는
  - RAID 1, RAID 0, RAID 5, RAID 10 과 같은 구성 방식 제공
  - 요금제는 시간 요금제만 제공한다. 
  - Init Script 사용이 가능하다
  - Oracle Linux가 제공된다.

 4. Agent를 설치해야한 사용할 수 있는 서비스
  - Cloud insight, System Security Checker, CLA

 5. 네이버클라우드 플래폼에서 제공하는 리젼(region)
  - 홍콩, 미국, 일본, 독일

 6. 네이버 클라우드 플랫폼에서 제공하는 전문화된 클라우드
  - 금융 클라우드, 민간 클라우드, 공공 클라우

 7. 콘솔에서 신청할 수 있는 서비스
  - 서버 이미지 생성, 스냅샷 기능, 모니터링 서비

 8. 서버 정지가 필요한 경우
  - 서버 스펙 변경, 서버 반

 9. 오토스케일링 설정 시 ASG에서 설정 가능한 내용
  - 오토스케일링에서 사용할 Launch Configuration, 서버 증가, 감소 정책, 알림 설정

 10. 네이버 클라우드 플랫폼 스토리지 추가
  - Linux의 LVM, Window는 동적디스크 할당을 통해 여러 개의 디스크를 하나의 볼륨으로 묶을 수 있다.
  - 서버에 연결된 디스크를 다른 서버로 옮길 수 있습니다.
  - 사용 중인 디스크의 크기가 부족한 경우, 최대 15개의 스토리지를 추가할 수 있습니다. 
  - 스토리지 당 10GB 단위로 사용자는 다양한 용량을 추가 가능

 11. GPU 서버는 VM에 최대 4개의 GPU를 제공할 수 있

 12. NCP VPC 환경에서 멀티존 이용이 가능한 상품
  - Cloud DB for MySQL, Load Balancer

 13. CDN+ 설정 시 설정 항목
  - Purge : CDN 캐시 서버에 저장되어 있는 컨텐츠를 삭제
  - Secure Token : 토큰 기반의 인증으로 허용된 접근에만 컨텐츠 접근
  - Ignore Query String : CDN 서비스가 원본 서버에 요청할 때 URL에 포함된 GET 파라미터를 제거한 후에 요청
  - Access Log : CDN 사용 로그를 확인할 수 있는 기능

 14. CDN을 함께 생성하는 기능이 있는 상품
  - Image Optimizer, Live station, VOD station

 15. VPC에서 사용 가능한 IP 대역은 172.17.0.0/16 이다.

 16. Image Optimizer에 대한 설명
  - 이미지 리사이즈 기능을 제공한다
  - 이미지 크롭 기능을 제공한다
  -이미지 자동회전 기능을 제공한

 17. 애플리케이션 로드밸런서의 특징
  - HTTP, HTTPS 프로토콜 지원
  - 고정 IP 제공
  - URL 기반 분기 가능
  -추가 설정 시 client IP 로깅 확인 가

 18. NPC의 VPC 환경에서 ACG 룰이 적용되는 장치는 서버NIC

 19. VPC 의 Subnet에 대한 설명
  - Private Subnet, Public Subnet이 있다.
  - 공인 IP가 필요한 로드밸런서는 Public Subnet에 위치
  - Private Subnet에 있는 서버들은 공인 IP 부여를 할 수 없음
 
 20. 이벤트 설정이 가능한 상품
  - Server, NAS

 21. Apache Kafka Cluster를 제공하는 서비스
  - Cloud Data Streaming Service

 22. Effective Log Search & Analytics의 로그전송 방법
  - Https SDK, IOS SDK, LOG SDK

 23. workplace에서 제공되는 기능
  - 결제시스템, 인사시스템, 메신져

 24. Cloud DB for MySQL에 관한 설명
  - 자동 Fail-over 제공
  - MySQL의 최대 백업 파일 보관은 30일이다
  - 최대 10개의 Slave DB를 생성할 수 있다
  - Slave DB로의 읽기 부하분산이 가능하다

 25. VPC 환경에서의 ACG에 대한 설명
  - 아웃바운드에 대한 설정이 가능하다
  - 접근 허용에 대한 룰을 설정한다
  - ACG 하나당 100개의 룰을 적용할 수 있다.
  - 서버는 최대 3개의 ACG를 맵핑할 수 있다.

 26. Security Monitoring에서 제공되는 항목
  - IDS, IPS, WAF

 27. Httpd를 설치하도록 init-script에 명령어
  - yum install -y httpd

 28. 마이크로서버에 대한 설명
  - Network Interface를 만들 수 없다
  - 1vCPU, 1GB 메모리이다
  - OS는 CentOS, Ubuntu를 지원한다
  - 결제수단 최초 등록 월부터 1년간 이용요금이 무

 29. 서버 정지가 필수인 기능
  - 서버 반납, 아닌것(내서버이미지, 스냅샷, 서버 이미지 빌더)

 30. Block Storage에 대한 설명
  - 데이터 손실 방지를 최우선으로 설계하여 모든 요소가 이중화
  - 2000GB까지 생성 가능하며, 서버 당 16개의 스토리지 사용
  -  기동 중단이나 성능 저하 없이 탄력적으로 성능 변경 가능
  - HDD/SDD 두 가지 타입으로 제공되며 적절한 선택이 중요

 31. 네이버 클라우드에서 제공하는 GPU 카드
  - P40, T4, V100

 32. 네이버 클라우드 플랫폼 서버에 스토리지 추가 할 경우 단일 스토리지 최대 용량
  - 2TB

 33. NCP에서 서버 생성하고 네트워크 구성 시 설명
  - 서버는 기본적으로 10.ㅌㅌㅌ/172.16ㅌㅌ/192.168.xx 대역 중 하나의 사설 IP를 부여받을 수 있다.
  - 서버의 사설망 네트워크 대역은 최소 28/ 부터 최대 16/ 범위
  - 서버는 기본적으로 1Gps 대역폭의 인터페이스를 생성한다

 34. 다음 중 Media 카테고리 상품
  - Live Station, VOD station, VOD Transcoder

 35. Load Balancer 상품에 대한 설명
  - Classic 플랫폼에서의 헬스체크 주기는 6초이다
  - Classic 플랫폼에서는 3번 응답이 없는 경우 Unbind 한다
  - VPC 플랫폼에서 한 대의 서버는 여러 Target Group에 포함될 수 있다.
  - VPC 플랫폼에서는 Target Group에서 헬스체크 주기를 수정할 수 있다
 
 36. VPC의 NACL에 대한 설명
  - Subnet 단위로 적용된다.
  - Allow Deny 규칙 모두 지원한다
  - 우선순위에 따라 규칙을 반영한다
 
 37. Load Balancer로 연결 가능한 프로토콜
  - TCP, HTTPS, SSL

 38. VPC 에서 Load balancer를 생성할 떄 타겟 그룹의 디폴트 포트 헬스체크 주기
  - 30초

 39. VPC 환경에서 서버 NIC 하나에 적용할 수 있는 ACG 갯수
  - 3개

 40. 로드밸런서에서 제공되는 로드 분배 알고리즘
  - RoundRobin, Least Connection, Source IP Hash

 41. VPC 환경에서 로드밸런서 중 SSL 인증을 지원하는 로드밸런서
  - 애플리케이션 로드밸런서

 42. VPC의 Private Subnet에 대한 설명
  - Private Subnet에 있는 서버들은 NAT GateWay를 통해 외부 인터넷으로 나갈 수 있습니다
  - 네이버 클라우드 플랫폼의 일부 상품들은 기본적으로 Public Subnet에 위치해야합니다
  - Private Subnet을 Public Subnet으로 전환할 수 없습
  - Live Station은 사용자가 라이브 방송 도중 일시정지를 하고 다시 재생이 가능하도록 타이머신 기능을 제공

 43. 네이버 클라우드 플랫폼에서 하나의 계정으로 만들 수 있는 최대 VPC 갯수 
  -3개
 
 44. Block Storage에서 제공하는 기능
  - Detach/attach 기능, snapshot 기능, disk 용량 증설

 45. Auto Scaling 구성 시 설정할 수 있는 항목
  - ACG, Load Balancer, VPC/Subnet

 46. vpc 환경에서 제공하는 로드밸런서 중 세션 유지가 필요한 TCP 기반 애플리케이션에서 이용할 수 있는 로드밸런서
  - 네트워크 프록시 로드밸런서
 
 47. Sysyem Security Checker에서 Linux 서버의 점검 항목
  - UMASK 설정 관리, 홈 디렉토리 권한 설정, Anonymous FTP 비활성화

 48. 네이버 클라우드 플랫폼 CLI를 이용하고자 할 때 사용하는 명령어 
  - Ncloud

 49. 클라우드의 특징
  - Scale in/out이 레거시 인프라보다 자유롭다
  = 요금은 사용량에 따른 종량제를 기본으로 하지만 상품에 따라 정액제 요금도 존재한다
  -사용할 수 있는 서버 OS가 제한된다

 50. VMware on Ncloud 상품의 카테고리
  - Hybrid & Private Cloud

 51. Live Station의 특징
  - 방송 서비스 구현에 꼭 필요한 Thumbnail image를 추출하고 직접 관리할 수 있음
  - Live Stations은 사용자가 라이브 방송 도중 일시정지하고 다시 재생 가능하도록 타임머신 기능을 제공
  - 라이브 방송 종료 후, 녹화 영상을 저장할 수 있음

 52. CDN+ 에 대한 설
  - 사용량에 따라 요금이 다르다
  - 요금은 전송량 + 일 수로 계산
  - CDN+ 와 GCDN은 요금 체계가 다르다

 53. Application 서비스 각각의 서비스 명과 설명
  - Clova Speech Recognition: 사람의 목소리를 텍스트로 바꿔주어 다양한 음성인식 서비스에 활용 가능
  - Clova Face Recognition : 이미지 속의 얼굴을 감지하고 인식하여 얻은 다양한 정보를 제공할 수 있는 서비스
  - papago NMT : 입력한 텍스틀르 대규모 학습 데이터를 기반으로 여러 나라의 언어로 자동 번역해 주는 서비스
 

 54. App Safer에서 앱 실행 환경 탐지가 가능한 부분
  - 루팅 탐지, 애플리케이션 변조 탐지, 메모리 변조 탐지

 55. 네이버 클라우드 플랫폼에서 운영하고 있는 채널
  - 블로그, 유튜브, 페이스북

 56. Cloud Log Analytics에 저장할 수 있는 최대 로그 용 - 100GB

 57. 메일 제목과 본문에서 스프레드 시트나 DB의 열 데이터를 순차적으로 입력하기 위한 기능
  - 변수 치환

 58. Cloud Log Analytics의 최대 저장 기간
  - 30

 59. 네이버 클라우드 플랫폼 챗봇 서비스와 채널 연동되는 서비스
  - 라인 톡톡 페이스북

 60. 네이버 클라우드 플랫폼 AI 서비스에서 제공하는 상품
  - Clova OCR, Clova Voice, Clova Face Recognition
