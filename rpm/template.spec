Name:           ros-indigo-schunk-canopen-driver
Version:        1.0.3
Release:        0%{?dist}
Summary:        ROS schunk_canopen_driver package

Group:          Development/Libraries
License:        FZI all rights reserved
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-fzi-icl-can
Requires:       ros-indigo-fzi-icl-core
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-joint-limits-interface
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-urdf
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-fzi-icl-can
BuildRequires:  ros-indigo-fzi-icl-core
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-joint-limits-interface
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-urdf

%description
The schunk_canopen_driver package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed May 04 2016 Georg Heppner <heppner@fzi.de> - 1.0.3-0
- Autogenerated by Bloom

* Mon May 02 2016 Felix Mauch <heppner@fzi.de> - 1.0.2-0
- Autogenerated by Bloom

