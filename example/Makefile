DEPDIR := .deps
DEPFLAGS = -MT $@ -MMD -MP -MF $(DEPDIR)/$*.d

COMPILE.c = $(CC) $(DEPFLAGS) $(CFLAGS) $(CPPFLAGS) $(TARGET_ARCH) -c

SUB_PROJECTS = test.gpj

ATKINS = "../atkins.py"

.PHONY = all

all: test.a

%.o : %.c
%.o : %.c $(DEPDIR)/%.d | $(DEPDIR)
	$(COMPILE.c) $(OUTPUT_OPTION) $<

%.d : %.gpj
	$(ATKINS) -MT $< -MMD -MP -MF $(DEPDIR)/$*.d

%.a : %.gpj
	$(ATKINS) -MT $< -MMD -MP -MF $(DEPDIR)/$*.d

$(DEPDIR): ; @mkdir -p $@

DEPFILES := $(SRCS:%.c=$(DEPDIR)/%.d)
DEPPROJECT := $(SUB_PROJECTS:%.gpj=$(DEPDIR)/%.d)

$(DEPFILES):
$(DEPPROJECT):

include $(wildcard $(DEPFILES))
include $(wildcard $(DEPPROJECT))
