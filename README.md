## das-2-2025-2

# Aula 30/07

- Apresentação do curso da AWS sobre arquitetura cloud

- AWS well architected: https://aws.amazon.com/pt/architecture/well-architected/
  Documento que traz boas práticas de arquitetura, vai ser mencionado durante o curso

- Papéis do arquiteto de nuvem:
  - Planejar: Analisar soluções para as necessidades e requisitos
  - Pesquisar: Fazer provas de conceito
  - Construir: Gerenciar a adoção do modelo

- Pilares do AWS Well Architected:
  1. Operational excellence: Run and monitor systems that deliver business value, Continually improve supporting processes and procedures, View the entire workload as code
  2. Security: Implement a strong identity foundation, Mantain traceability, Implement risk assessment and mitigation strategies
  3. Reliability: Recover quickly, Dynamically meet compute demand, Mitigate disruptions
  4. Performance Effiency: Choose and maintain efficient resources, Democratize advanced technologies, Employ mechanical Sympathy
  5. Cost optimization: Measure effiency, Eliminate unneeded expense, Adopt the right consumption model, Consider using managed services
  6. Sustainability: Establish sustainability goals, Maximize utilization, Choose efficient hardware and software, Reduce downstream impact

- Implementando escalabilidade
- Automatizando o ambiente

# Aula 06/08 

- Regiões e AZs

- Pilares de segurança

- Princípio do privilégio mínimo

- Server encryption

- Autenticação x autorização

# Aula 13/08

- Determining permissions at the time of request

- IAM policy document structure
    - Version
    - Statement
    - Effect
    - Principal
    - Action
    - Resource
    - Condition
- [Module 2 Knowledge Check](https://awsacademy.instructure.com/courses/113113/assignments/1270651?module_item_id=10653588)
- [Guided Lab: Exploring AWS Identity and Access Management (IAM)](https://awsacademy.instructure.com/courses/113113/assignments/1270605?module_item_id=10653616)
- [Module 3 Knowledge Check](https://awsacademy.instructure.com/courses/113113/assignments/1270652?module_item_id=10653624)

# Aula 20/08

- Amazon S3
  - Benefits
      - Durability
      - Availability
      - High Performance
      
- [lab: Creating a Static Website for the Cafe](https://awsacademy.instructure.com/courses/129676/assignments/1485129?module_item_id=12389220)
   
- Good for:
  - Spikes in demand
  - Static site
  - Financial analysis

# Aula 27/08

- revisão S3 e buckets
- Escolhendo regioes
  - proximidade, legislação local...
 
- indo pro git

# Aula 03/09

- EC2
  - Foco em processamento, S3 = arquivos "fixos", EC2 permite paginas dinamicas
  - VMs, VPS
 
# Aula 10/09

- https://aws.amazon.com/pt/ec2/instance-types/

- Instance store
- Amazon EBS
- Amazon Elastic File System (EFS)

- Subindo EC2 Windows

# Aula 17/09

- Retrieving instance metadata
- AMI deployment models
- Amazon VPC
- Network address translation (NAT) gateway
- Amazon route 53
  - 
 
- Sandbox 
- Servidor minecraft na EC2

# Aula 24/09

- 3 laboratorioses:
- [Guided lab: Creating a Virtual Private Cloud](https://awsacademy.instructure.com/courses/129676/assignments/1485156?module_item_id=12389305)
- [Challenge (Cafe) lab: Creating a VPC Networking Environment for the Café](https://awsacademy.instructure.com/courses/129676/assignments/1485132?module_item_id=12389306)
- [Module 7 Knowledge Check](https://awsacademy.instructure.com/courses/129676/assignments/1485196?module_item_id=12389310)


# Aula 01/10



# 2 Bimestre

## Aula 08/10/2025
- RBAC x ABAC
- Identidade Federada
- Criptografia Simétrica x Assimétrica
- Detecção de vulnerabilidade estática
- Detecção de intrusão
- [Guided lab: Creating a VPC Peering Connection](https://awsacademy.instructure.com/courses/129676/assignments/1485154?module_item_id=12389321)
- 30/30 no lab

## Aula 15/10/2025


- Monitoramento de performance, metricas (cpu, read/write, upload/download, nao da pra ver memoria), logs
- tracing (rastreia todo o caminho de uma requisição atraves dos serviços)
- elasticidade
- escalabilidade horizontal
- load balancers
- [Guided lab: Creating a Highly Available Environment](https://awsacademy.instructure.com/courses/129676/assignments/1485152?module_item_id=12389382)
ami-0ea2f9b8b959a8d12


## Aula 22/10/2025

- Module 11: Automating Your Architecture
- [Guided lab: Automating Infrastructure with AWS CloudFormation](https://awsacademy.instructure.com/courses/129676/assignments/1485149?module_item_id=12389414)
- Route 53: DNS da AWS

## Aula 29/10/2025

- Module 12: Caching Content
- [Module 12 Knowledge Check](https://awsacademy.instructure.com/courses/129676/assignments/1485174?module_item_id=12389441)
- CDN
- Distrubuicao de conteudo, imagens, videos, paginas web, entregues ao usuario conforme sua localizacao geografica
- Cloudfront global edge: muitas edge locations para entregar conteudo com baixa latencia (especialmente streaming)

  
## Aula 05/11/2025

- Module 13: Building Decoupled Architectures
- [Guided lab: Building Decoupled Applications by Using Amazon SQS](https://awsacademy.instructure.com/courses/129676/assignments/1485150?module_item_id=12389450)
- Lab dessa aula estava quebrado por descontinuidade de um recurso da AWS necessário
- Point to point messaging
- Loose coupling, componentes independentes, que em caso de falhas não derrubam o sistema completo.



## Aula 12/11/2025

- Module 14: Building Serverless Architectures and Microservices
- [Guided lab: Implementing a Serverless Architecture on AWS](https://awsacademy.instructure.com/courses/129676/modules/items/12389475)

- AWS Serverless servies (Lambda, DynamoDB, etc.)
- Sem necessidade de gerenciar um servidor completo para rodar funcoes
