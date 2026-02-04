# Dynamics 365 Contact Center - Architecture Map

## Architecture Flow Overview

The D365 Contact Center architecture follows a hierarchical flow:

**CHANNELS → WORKSTREAMS → ROUTING RULES → QUEUES → AGENTS**

Each layer adds intelligence, context, and control to ensure optimal customer service delivery through AI-powered routing and intelligent work distribution.

---

## Visual Architecture Flow

### 📱 CHANNELS - Customer Engagement Layer

Communication entry points for customer engagement across multiple mediums:

- **Voice** - PSTN calls via Azure Communication Services
- **Chat** - Live chat support with web widget integration
- **SMS** - Text messaging via Azure Communication Services or Twilio
- **Social** - Facebook, WhatsApp, Apple Messages for Business, LINE
- **Teams** - Microsoft Teams native integration
- **Custom** - Custom messaging channels and integrations
- **Records** - Cases, emails, and entity records

**Phone Numbers:** Each phone number connects to a voice channel within a workstream. A workstream can have multiple voice channels with different phone numbers (e.g., for multilingual support).

### 🔄 WORKSTREAMS - Routing & Configuration Layer

Containers that enrich, route, and configure work item behavior:

**Types:**
- **Messaging Workstream** → Routes: Chat, SMS, Social, Teams
- **Voice Workstream** → Routes: Phone calls (Push mode only)
- **Record Workstream** → Routes: Cases, Emails, Records

**Work Distribution Modes:**
- **Push:** Auto-assign to agents with alerts (required for voice)
- **Pick:** Agents manually select work items

**Configuration:**
- Capacity settings (unit-based or profile-based)
- Allowed presences (Available, Busy, etc.)
- Skill matching algorithm (Exact, Closest, None)
- Session templates and agent notifications
- Context variables and representative affinity
- Auto-close settings and wrap-up time

### 🎯 ROUTING RULES - Intelligent Routing Layer

**Classification Rules:**
- Categorize incoming work items
- Add context and metadata
- Evaluate customer parameters

**Route-to-Queue Rules:**
- Condition-based routing logic
- Priority-based assignments
- Skill-based matching
- Multiple rules per workstream

**Fallback Queue:**
Safety net for work items when:
- No route-to-queue rules match
- Classification or routing errors occur

### 📥 QUEUES - Work Distribution Layer

Collections that organize and distribute work items:

**Queue Types (matched to workstream channel type):**
- **Messaging Queue** → Holds: Chat, SMS, Social messages
- **Voice Queue** → Holds: Phone calls
- **Record Queue** → Holds: Cases, Emails, Records

**Assignment Methods:**
1. **Highest Capacity** - Routes to agent with most capacity
2. **Round Robin** - Rotates based on membership order
3. **Least Active** - Routes to least recently active agent
4. **Custom Assignment** - Rule-based (priority, severity, capacity)

**Configuration:**
- Queue Priority (numeric: lower = higher priority)
- Operating Hours (schedules & time zones)
- Overflow Management (redirect when threshold exceeded)
- Agent membership

**Default Queues (system-defined):**
- Default messaging queue
- Default voice queue
- Default entity queue

### ⚙️ ASSIGNMENT ALGORITHM - Evaluation Layer

The assignment algorithm evaluates multiple factors:

- **Skills** - Exact match, closest match, or none
- **Presence** - Available, Busy, Do Not Disturb
- **Capacity** - Current workload vs. max capacity (unit-based or profile-based)
- **Queue Membership** - Agent must be in the queue
- **Priority & Rules** - From workstream configuration

### 👥 AGENTS - Service Representative Layer

Service representatives who handle customer interactions:

**Agent Configuration:**
- Assigned to one or more queues
- Capacity profile (defines workload capacity)
- Skills (for skill-based routing)
- Presence status (Available, Busy, Away, etc.)
- Channel-specific capacity

**Agent Experience:**
- **Push mode:** Receives auto-assigned work with notifications
- **Pick mode:** Manually selects from "Open work items"
- **Representative affinity:** Same agent handles returning work items
- **Wrap-up time:** Capacity blocked after completing work

---

## 🔗 Key Relationships

### ⬇️ Top-Down Relationships (Architecture Flow)

#### 1. Channel → Workstream (Many-to-One)
- **Forward:** Multiple channels of the SAME type can share one workstream
- **Example:** 3 chat channels → 1 messaging workstream
- **Reverse:** ✅ A workstream can have MULTIPLE channels attached (of the same type)

#### 2. Phone Number → Voice Channel → Workstream (Many-to-One)
- **Forward:** Each phone number is associated with exactly ONE voice channel, which belongs to ONE workstream
- **Constraint:** Phone numbers must have inbound calls enabled and cannot be shared across workstreams
- **Reverse:** ✅ A workstream CAN have MULTIPLE voice channels, each with a different phone number
- **Use Case:** Multilingual support - configure multiple voice channels with different phone numbers for different languages (e.g., Spanish number, German number, French number all in one workstream)

#### 3. Workstream → Queues (One-to-Many)
- **Forward:** One workstream can route to multiple queues via route-to-queue rules
- **Required:** Must have one fallback queue as safety net
- **Reverse:** ✅ A queue CAN receive work from MULTIPLE workstreams (of matching channel type)
- **Example:** A "VIP Voice Queue" can receive calls from both "Premium Support Workstream" and "Executive Support Workstream"

#### 4. Queue → Agents (Many-to-Many)
- **Forward:** Queues can have multiple agents as members
- **Reverse:** ✅ Agents CAN be members of MULTIPLE queues
- **Distribution:** Based on assignment method and availability
- **Example:** Agent John can be in "Voice Queue", "Chat Queue", and "VIP Queue" simultaneously

### ⬆️ Bottom-Up Relationships (Reverse Flow)

#### Agent Perspective:
- ✅ An agent can be a member of **multiple queues**
- ✅ An agent receives work from **all queues they belong to**
- ✅ Work assignment depends on capacity, skills, and presence across all queues
- 📊 Agents can view work items from all their queues in the Omnichannel Agent Dashboard
- **Example:** Agent Sarah in "Voice Queue", "VIP Chat Queue", and "Email Queue"

#### Queue Perspective:
- ✅ A queue can receive work from **multiple workstreams** (matching channel type)
- ✅ A queue can have **multiple agents** as members
- ✅ A queue can be a fallback queue for **multiple workstreams**
- ❌ A queue CANNOT receive work from workstreams of **different channel types**
- **Example:** "Premium Support Voice Queue" receives calls from both "Executive Support Workstream" and "VIP Customer Workstream"

#### Workstream Perspective:
- ✅ A workstream can have **multiple channels** of the same type attached
- ✅ A workstream can route to **multiple queues**
- ✅ A workstream can use the same queue as **other workstreams**
- ✅ A voice workstream can have **MULTIPLE phone numbers** through multiple voice channels
- 💡 Common use case: Multiple voice channels with different phone numbers for multilingual support

#### Channel Perspective:
- 📌 A channel belongs to **ONE workstream** (based on configuration flow)
- ✅ Multiple channels of the same type can share one workstream
- **Example:** 3 different chat widget channels → all in 1 messaging workstream

### 🔒 Type Constraints

**Workstream → Channel Type Constraint:**
- Messaging workstream → Messaging queues only
- Voice workstream → Voice queues only
- Record workstream → Record queues only
- ❌ Cross-type routing NOT allowed
- ✅ Multiple workstreams of the same type CAN share the same queue

**Workstream Type → Distribution Mode:**
- Voice: Push mode ONLY
- Messaging: Push or Pick mode
- Record: Push or Pick mode
- ⚠️ Mode CANNOT be changed after creation

### 📊 Relationship Summary Table

| From | To | Cardinality | Can Reverse? |
|------|-----|-------------|--------------|
| Channel | Workstream | Many-to-One | ✅ Yes (One workstream → Many channels) |
| Phone Number | Voice Channel | One-to-One | ❌ No (Each phone number → One voice channel only) |
| Voice Channel | Workstream | Many-to-One | ✅ Yes (One workstream ← Many voice channels with different phone numbers) |
| Workstream | Queue | One-to-Many | ✅ Yes (One queue ← Many workstreams) |
| Queue | Agent | Many-to-Many | ✅ Yes (fully bidirectional) |

---

## Phone Numbers Configuration

### Relationship Architecture
**Phone Number → Voice Channel → Workstream**

- Each phone number is associated with exactly ONE voice channel
- Each voice channel belongs to ONE workstream
- ✅ One workstream CAN have MULTIPLE voice channels (each with different phone numbers)

### Configuration Steps
1. **Provision:** Acquire phone numbers via Azure Communication Services
2. **Enable:** Enable inbound calls on the phone numbers
3. **Create Voice Channels:** In the workstream, create multiple voice channels (one per phone number)
4. **Associate:** Link each phone number to its respective voice channel in the workstream
5. **Configure:** Set up language settings and voice profiles for each channel

### Multiple Phone Numbers per Workstream
**Use Case:** Multilingual Support
- Create multiple voice channels within one workstream
- Each voice channel has a different phone number
- Each voice channel configured with a different primary language
- **Example:** +1-555-0100 (Spanish), +1-555-0200 (German), +1-555-0300 (French) all in one workstream

### Single Phone Number - Multiple Languages
Alternatively, one phone number can support multiple languages with:
- Primary language (first greeting)
- Additional language options for customers
- Hold and wait music configuration per language
- Voice profile settings (voice, style, speed, pitch) per language

### Constraints
- Only numbers with inbound calls enabled are available
- Each phone number can only be in ONE voice channel
- Cannot associate number already linked to another workstream
- Anonymous calls only supported via Azure Direct Routing
- Cannot edit or upgrade phone number features after connecting to workstream

---

## 🔄 Routing Flow Example

**Complete Call Routing Journey:**

1. **Customer Action:** Customer calls +1-555-0100

2. **Phone Number Lookup:** Phone Number (+1-555-0100) associated with "Premium Support Voice Workstream"

3. **Classification:** Classification Rules evaluate call context (customer type, product, history)

4. **Route-to-Queue Decision:**
   - Rule 1: If customer = "Premium" → "VIP Voice Queue"
   - Rule 2: If product = "Product A" → "Product A Voice Queue"
   - No match → "Fallback Voice Queue"

5. **Queue Processing:** Queue receives call and applies assignment method (e.g., Highest Capacity)

6. **Agent Evaluation:** Assignment algorithm evaluates:
   - Agent presence (Available, Busy, DND)
   - Agent capacity (current workload vs. max)
   - Agent skills (if skill matching enabled)
   - Queue membership

7. **Assignment:** Call assigned to Agent with highest capacity + matching skills + allowed presence

8. **Agent Notification:** Agent receives notification and call appears in workspace with full context

9. **Post-Call:** After call ends, agent enters wrap-up time (capacity blocked for configured duration)

---

## ⚠️ Important Constraints

✓ Unified routing must be enabled for Record workstreams

✓ Work distribution mode (Push/Pick) CANNOT be changed after workstream creation

✓ Voice workstreams support PUSH mode ONLY

✓ Phone numbers can only be associated with ONE voice channel at a time

✓ Queues and workstreams must have matching channel types

✓ Cross-queue transfers only allowed within same channel type

✓ Bots receive conversations only in push-based workstreams

✓ Representative affinity only applies to push-type work distribution

✓ System Administrator role OR secure column permissions required for configuration

---

## 🤖 AI & Intelligence Features

### Unified Intelligent Routing (AI-Infused)
- **Sentiment Analysis** - Real-time emotion detection
- **Predicted Effort** - AI estimates complexity
- **Skills Matching** - Intelligent capability matching
- **Presence Awareness** - Real-time availability tracking
- **Capacity Optimization** - Dynamic workload balancing
- **Customer Parameters** - Historical data evaluation

### Agent Copilot Features
- **Knowledge Chat/Search** - Q&A format knowledge retrieval
- **Agent Prompting** - AI-powered suggestions
- **Email Draft Generation** - Automated response drafting
- **Case Summary Generation** - AI-generated summaries
- **Conversation Summaries** - Automatic recap
- **Live Call Transcription** - Real-time transcription
- **Call Sentiment Analysis** - Continuous monitoring

---

## 🔧 Supporting Components

### Bots
- Connected from Copilot Studio
- Push-based workstreams only
- Pre-conversation automation
- Handoff to human agents

### Templates
- Session templates
- Notification templates
- Consistent agent experience
- Customizable layouts

### Context Variables
- Custom data passing
- Through routing pipeline
- Available to agents
- Integration support

### Operating Hours
- Queue-based schedules
- Time zone support
- Business hours routing
- After-hours handling

### Capacity Profiles
- Define agent workload limits
- Channel-specific capacity
- Unit or profile-based
- Dynamic adjustment

### Smart Assist
- AI-powered suggestions
- Knowledge article recommendations
- Quick replies library
- Real-time assistance

---

## 📐 Configuration Hierarchy

```
Organization/Environment
    │
    ├─ Channels (provision & configure)
    │   ├─ Voice Channel
    │   │   └─ Phone Numbers (acquire via Azure Communication Services)
    │   ├─ Chat Channel
    │   ├─ SMS Channel (Azure Communication Services or Twilio)
    │   ├─ Social Channels (Facebook, WhatsApp, Apple Messages, LINE)
    │   ├─ Microsoft Teams
    │   └─ Custom Messaging Channels
    │
    ├─ Workstreams (create & configure)
    │   ├─ Type selection (Messaging, Voice, Record)
    │   ├─ Channel association (attach channels)
    │   ├─ Work distribution mode (Push or Pick)
    │   ├─ Capacity settings
    │   ├─ Allowed presences
    │   ├─ Skill matching algorithm
    │   ├─ Classification rules
    │   ├─ Route-to-queue rules
    │   └─ Fallback queue
    │
    ├─ Queues (create & configure)
    │   ├─ Queue type (Messaging, Voice, Record)
    │   ├─ Assignment method
    │   ├─ Priority
    │   ├─ Operating hours
    │   ├─ Overflow management
    │   └─ Agent membership
    │
    ├─ Agents/Representatives (configure)
    │   ├─ Queue assignments
    │   ├─ Capacity profile
    │   ├─ Skills
    │   └─ Presence management
    │
    └─ Supporting Components
        ├─ Capacity Profiles
        ├─ Session Templates
        ├─ Notification Templates
        ├─ Context Variables
        ├─ Operating Hours
        ├─ Bots/Agents (Copilot Studio)
        └─ Smart Assist configurations
```

---

## Summary

The D365 Contact Center architecture supports omnichannel customer service with:

- **Multiple entry points** through diverse channels
- **Intelligent routing** with AI-powered decision making
- **Flexible workstreams** supporting multilingual and multi-channel scenarios
- **Dynamic work distribution** based on skills, capacity, and presence
- **Agent empowerment** with AI-assisted tools and insights
- **Bidirectional relationships** allowing complex routing scenarios

This unified architecture enables organizations to deliver exceptional customer service across all touchpoints with optimal resource utilization and intelligent automation.

---

## 📚 Documentation Sources

All information sourced from official Microsoft Learn documentation:

- [Create and manage workstreams](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/create-workstreams)
- [Create and manage queues for unified routing](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/queues-omnichannel)
- [Set up inbound calling for the voice channel](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/voice-channel-inbound-calling)
- [Manage phone numbers](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/voice-channel-manage-phone-numbers)
- [Configure multilingual voice agents](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/configure-multilingual-agents)
- [Overview of channels](https://learn.microsoft.com/en-us/dynamics365/customer-service/use/channels)
- [Contact center architecture reference](https://learn.microsoft.com/en-us/dynamics365/guidance/reference-architectures/contact-center-dynamics-365-customer-service-enterprise)
- [Omnichannel Agent Dashboard](https://learn.microsoft.com/en-us/dynamics365/customer-service/use/oc-agent-dashboard)

**Created:** February 2026
**Version:** 2.0 (Corrected and Enhanced)
