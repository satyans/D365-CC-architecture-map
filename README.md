# Dynamics 365 Contact Center - Architecture Map

An interactive visual guide to Dynamics 365 Contact Center architecture, showing relationships between channels, workstreams, queues, and agents.

## 🌐 Live Demo

**View the interactive website**: [https://satyans.github.io/D365-CC-architecture-map/](https://satyans.github.io/D365-CC-architecture-map/)

## 📋 Overview

This repository contains comprehensive documentation and interactive visualizations of the D365 Contact Center architecture, including:

- **Interactive Website** with Fluent Design patterns
- **Detailed Documentation** in markdown and PDF formats
- **Relationship Mapping** showing all component connections
- **Configuration Examples** with practical use cases

## 🎯 Key Features

### Interactive Architecture Map
- Modern, responsive web interface with Microsoft Fluent Design
- Expandable/collapsible sections for easy navigation
- Search functionality to find specific components
- Hover effects with reveal lighting
- Keyboard shortcuts for quick access

### Comprehensive Coverage
- **7 Channel Types**: Voice, Chat, SMS, Social, Teams, Custom, Records
- **3 Workstream Types**: Messaging, Voice, Record
- **Queue Management**: Assignment methods, priorities, overflow handling
- **Agent Configuration**: Capacity, skills, presence management
- **AI Features**: Intelligent routing, sentiment analysis, Copilot assistance

### Accurate Relationships
- Top-down architecture flow (Channels → Workstreams → Queues → Agents)
- Bottom-up reverse relationships
- Many-to-many, one-to-many, and one-to-one mappings
- Type constraints and configuration rules

## 📁 Files

- **`index.html`** - Interactive website with full architecture visualization (hosted on GitHub Pages)
- **`architecture-infographic.html`** - Single-page visual infographic summarizing architecture and relationships
- **`D365-Contact-Center-Architecture-Infographic.png`** - High-resolution infographic image (793 KB)
- **`D365-Contact-Center-Architecture-Map.md`** - Complete documentation in markdown
- **`D365-Contact-Center-Architecture-Map.pdf`** - PDF version for offline reference
- **`convert_to_pdf.py`** - Python script to regenerate PDF from markdown
- **`html_to_png.py`** - Python script to convert HTML infographic to PNG

## 🚀 Quick Start

### View Online (Recommended)
Visit the live website: **[https://satyans.github.io/D365-CC-architecture-map/](https://satyans.github.io/D365-CC-architecture-map/)**

### View the Infographic
Quick visual summary: **[Architecture Infographic](./D365-Contact-Center-Architecture-Infographic.png)**

### View Locally
1. Clone the repository: `git clone https://github.com/satyans/D365-CC-architecture-map.git`
2. Open `index.html` in any modern web browser
3. Use the Expand/Collapse buttons to navigate sections
4. Try the search box to find specific topics
5. Hover over cards and sections to see Fluent Design effects

### Keyboard Shortcuts
- **Ctrl/Cmd + E** - Expand all sections
- **Ctrl/Cmd + C** - Collapse all sections
- **Ctrl/Cmd + F** - Focus search box

## 📖 Architecture Layers

### 1. Channels (Customer Engagement)
Entry points for customer interactions across multiple communication mediums.

### 2. Workstreams (Routing & Configuration)
Containers that enrich, route, and assign work items with configurable rules.

### 3. Routing Rules (Intelligent Routing)
Classification and route-to-queue rules with AI-powered decision making.

### 4. Queues (Work Distribution)
Collections that organize and distribute work items to agents.

### 5. Assignment Algorithm (Evaluation)
Evaluates skills, presence, capacity, and rules for optimal agent selection.

### 6. Agents (Service Representatives)
Representatives who handle customer interactions with AI assistance.

## 🔗 Key Relationships

- **Channel → Workstream**: Many-to-One (multiple channels can share one workstream)
- **Phone Number → Voice Channel → Workstream**: Many-to-One (workstream can have multiple phone numbers via multiple voice channels)
- **Workstream → Queue**: One-to-Many (workstream routes to multiple queues)
- **Queue → Agent**: Many-to-Many (agents can be in multiple queues)

## 📚 Documentation Sources

All information is sourced from official Microsoft Learn documentation:

- [Create and manage workstreams](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/create-workstreams)
- [Create and manage queues for unified routing](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/queues-omnichannel)
- [Set up inbound calling for the voice channel](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/voice-channel-inbound-calling)
- [Configure multilingual voice agents](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/configure-multilingual-agents)
- [Overview of channels](https://learn.microsoft.com/en-us/dynamics365/customer-service/use/channels)
- [Contact center architecture reference](https://learn.microsoft.com/en-us/dynamics365/guidance/reference-architectures/contact-center-dynamics-365-customer-service-enterprise)

## 🛠️ Technical Details

### Technologies Used
- HTML5, CSS3, JavaScript (Vanilla - no dependencies)
- Microsoft Fluent Design System
- Python 3.x with reportlab for PDF generation

### Design Features
- Acrylic material effects with backdrop blur
- Reveal lighting that follows cursor movement
- Smooth cubic-bezier animations
- Responsive grid layouts
- Microsoft color palette and typography

## 📝 Version History

**Version 2.0** (February 2026) - Current
- Corrected phone number to workstream relationships
- Enhanced visual architecture flow with prominent layer labels
- Moved Key Relationships section after architecture flow
- Added reverse relationship mappings
- Updated all documentation with verified information

**Version 1.0** (February 2026) - Initial
- Initial release with basic architecture map
- Interactive website with Fluent Design
- PDF and markdown documentation

## 🤝 Contributing

This documentation is based on official Microsoft Learn resources. For updates or corrections:
1. Verify information against official documentation
2. Update markdown file with corrections
3. Regenerate PDF using `python convert_to_pdf.py`
4. Test interactive website in multiple browsers

## 📄 License

This documentation is for educational and reference purposes. Microsoft Dynamics 365 and related trademarks are property of Microsoft Corporation.

## 👤 Author

Created by Satyan S - Expert in D365 Contact Center architecture and configuration

---

**Last Updated:** February 5, 2026
**Status:** Complete and Verified
